from notifications_python_client.notifications import NotificationsAPIClient
from dotenv import load_dotenv
import os
import argparse
import re

load_dotenv()

DEFAULT_TEMPLATE_IDS = {
    "6aa04f0d-94c2-4a6b-af97-a7369a12f681": "consent-request-hpv.md",
    "ceefd526-d44c-4561-b0d2-c9ef4ccaba4f": "consent-reminder-hpv.md",
    "017853bc-2b35-4aff-99b1-193e514613a0": "consent-request-flu.md",
    "7f85a5b4-5240-4ae9-94f7-43913852943c": "consent-reminder-flu.md",
    "7e86e688-ceca-4dcc-a1cf-19cb559d38a8": "consent-request-mmr.md",
    "5462c441-81c0-4ac0-821f-713b4178f8ba": "consent-reminder-mmr.md",
    "9b1a015d-6caa-47c5-a223-f72377586602": "consent-request-doubles.md",
    "3523d4b8-530b-42dd-8b9b-7fed8d1dfff1": "consent-reminder-doubles.md",
    "c7bd8150-d09e-4607-817d-db75c9a6a966": "consent-request.md",
    "b9c0c3fb-24f1-4647-a2a1-87389cec9942": "consent-reminder.md"
}


def get_govuk_client() -> NotificationsAPIClient:
    api_key = os.getenv('NOTIFY_API_KEY')
    return NotificationsAPIClient(api_key)

def replace_underscored_variables(text: str) -> str:
    """Replace variables like subteam__name with 'subteam name'"""
    def replace_match(match):
        var_name = match.group(1)
        # Replace underscores with spaces
        readable_name = var_name.replace('__', ' ').replace('_', ' ')
        return f"(({readable_name}))"
    
    # Match ((variable_name)) patterns
    return re.sub(r"\(\(([a-zA-Z0-9_]+)\)\)", replace_match, text)

def convert_to_markdown(body: str) -> str:
    if not body:
        return body

    # Replace CRLF with LF
    body = body.replace("\r\n", "\n")

    # Replace underscored variables before other replacements
    body = replace_underscored_variables(body)

    # Replace (((...))) with (==...==)
    body = re.sub(r"\(\(\((.*?)\)\)\)", r"(==\1==)", body)

    # Replace ((...)) with ==...==
    body = re.sub(r"\(\((.*?)\)\)", r"==\1==", body)

    # Remove conditional blocks with ??
    body = re.sub(r"==\w+\?\?.*?==", "", body)

    # Convert all ## to ### (demote headings)
    body = re.sub(r"^##\s?", "### ", body, flags=re.MULTILINE)

    # Replace ^ with > if it's at the start of a line
    body = re.sub(r"^\^\s?", "> [!NOTE]\n> ", body, flags=re.MULTILINE)

    return body


def compose_yaml_frontmatter(frontmatter: dict[str, str|int]) -> str:
    yaml_lines = ["---"]
    for key, value in frontmatter.items():
        yaml_lines.append(f"{key}: {value}")
    yaml_lines.append("---\n")
    return "\n".join(yaml_lines)
    
def extract_frontmatter(file_path: str) -> dict[str, str | int]:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Extract frontmatter section
        parts = content.split("---", 2)
        if len(parts) < 3:
            return {}
        
        frontmatter = parts[1]
        result = {}
        
        # Find all key-value pairs
        for line in frontmatter.strip().split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()
                # Try to convert to int if it's a number
                if value.isdigit():
                    result[key] = int(value)
                else:
                    result[key] = value
        
        return result
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {}

def strip_square_brackets(text: str) -> str:
    return re.sub(r"^\[.*?]\s*", "", text)

def get_file_name(template: dict[str, str|int]) -> str:
    file_name = f"{DEFAULT_TEMPLATE_IDS.get(template.get("id", ""))}"

    return file_name

from textwrap import dedent

def talk_to_your_child_message() -> str:
    return (
        "### Talk to your child about what they want\n"
        "\n"
        "We suggest you talk to your child about the vaccinations before you "
        "respond to us.\n"
        "\n"
        "Young people have the right to refuse vaccinations. Those who show "
        "['Gillick competence'](https://www.nhs.uk/conditions/consent-to-treatment/children/) "
        "have the right to consent to vaccinations themselves. Our team may "
        "assess Gillick competence during vaccination sessions.\n"
    )


def update_templates(template_ids: list[str], output_dir: str, order_start: int=0) -> None:
    notifications_client = get_govuk_client()

    current_order = order_start

    for template_id in template_ids:
        print(f"Updating template with ID: {template_id}")

        # Get the template from GOV.UK Notify
        template: dict[str, str|int] = notifications_client.get_template(
            template_id=template_id,
        )

        # Get the output file path
        output_file = os.path.join(output_dir, get_file_name(template))

        # Extract existing frontmatter
        existing_frontmatter = extract_frontmatter(output_file)
        existing_title = existing_frontmatter.get("title", "")
        existing_order = existing_frontmatter.get("order", None)

        # Use existing values if available, otherwise use defaults
        title = existing_title if existing_title else strip_square_brackets(template.get("name", ""))
        order = existing_order if existing_order is not None else current_order

        # Build YAML front matter - required fields
        frontmatter = {
            "layout": "email-template" if template.get("type", "email") == "email" else "text-message-template",
            "title": title,
            "theme": "Emails to parents" if template.get("type", "email") == "email" else "Text messages to parents",
        }
        
        # Only add subject if it exists in existing frontmatter
        if "subject" in existing_frontmatter:
            frontmatter["subject"] = convert_to_markdown(template.get("subject", ""))
        
        # Only add toReplacePlaceholders if it exists in existing frontmatter
        if "toReplacePlaceholders" in existing_frontmatter:
            frontmatter["toReplacePlaceholders"] = existing_frontmatter["toReplacePlaceholders"]
        
        # Add order last
        frontmatter["order"] = order

        yaml_content = compose_yaml_frontmatter(frontmatter)

        # Get and process the body
        body_content = convert_to_markdown(template.get("body", ""))

        body_content = re.sub("==talk to your child message==", talk_to_your_child_message(), body_content)

        # Combine YAML front matter and processed body
        md_content = yaml_content + "\n" + body_content

        # Create output file path
        output_file = os.path.join(output_dir, get_file_name(template))

        # Write out to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(md_content)

        current_order += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Update the email templates using the Notify API."
    )
    parser.add_argument(
        "--template_ids",
        help="A list of GUIDs of the templates to update, comma separated. Defaults to values in DEFAULT_TEMPLATE_IDS.",
        default=",".join(DEFAULT_TEMPLATE_IDS)
    )
    parser.add_argument(
        "--output_dir",
        help="The directory to output the updated templates to.",
        default="../../app/email-and-text-templates"
    )
    parser.add_argument(
        "--order_start",
        help="The starting order number for the templates.",
        default=40
    )
    args = parser.parse_args()

    template_ids = args.template_ids.split(',')
    template_ids = [template_id.strip() for template_id in template_ids]

    update_templates(template_ids, args.output_dir, args.order_start)
