from notifications_python_client.notifications import NotificationsAPIClient
from dotenv import load_dotenv
import os
import argparse
import re

load_dotenv()

DEFAULT_TEMPLATE_IDS = {
    # Emails to parents
    "017853bc-2b35-4aff-99b1-193e514613a0": "parent-emails/consent-request-flu.md",
    "7b9bb010-0742-460a-ae25-1922355b6776": "parent-emails/consent-request-hpv.md",
    "9b1a015d-6caa-47c5-a223-f72377586602": "parent-emails/consent-request-doubles.md",
    "7e86e688-ceca-4dcc-a1cf-19cb559d38a8": "parent-emails/consent-request-mmr.md",
    "c6c8dbfc-b429-4468-bd0b-176e771b5a8e": "parent-emails/consent-confirm-given.md",
    "5a676dac-3385-49e4-98c2-fc6b45b5a851": "parent-emails/consent-confirm-refused.md",
    "35d621db-957b-4afb-9143-3e32398d2b87": "parent-emails/consent-confirm-needs-triage.md",
    "1d050527-9a6c-4513-86d4-6955b98ac7d9": "parent-emails/consent-confirm-moved-school.md",
    "6d746839-a20e-4d50-8a1d-6f3900ff69b2": "parent-emails/consent-unknown-parent-details.md",
    "279c517c-4c52-4a69-96cb-31355bfa4e21": "parent-emails/triage-vaccinate.md",
    "279c517c-4c52-4a69-96cb-31355bfa4e21": "parent-emails/triage-do-not-vaccinate.md",
    "0e37d12a-5469-4ad2-aa09-83e0ef56e03e": "parent-emails/triage-delay-vaccination.md",
    "3c7461bd-e3cf-4ff9-9053-b4e87490aa45": "parent-emails/triage-invite-to-clinic.md",
    "8b8a9566-bb03-4b3c-8abc-5bd5a4b8797d": "parent-emails/session-reminder.md",
    "7238ee27-5840-40e5-b9b9-3130ba4cd4fa": "parent-emails/session-vaccination-given-flu.md",
    "8a65d7b5-045c-4f26-8f76-6e593c14cb6d": "parent-emails/session-vaccination-given-hpv.md",
    "38727494-9a81-42b3-9c1f-5c31e55333e7": "parent-emails/session-vaccination-given-menacwy.md",
    "3abe7ca8-a889-484b-ab9f-07523302eb6a": "parent-emails/session-vaccination-given-td-ipv.md",
    "0b1095db-fb38-4105-9f01-a364fa8bbb1c": "parent-emails/session-vaccination-given-mmr.md",
    "130fe52a-014a-45dd-9f53-8e65c1b8bb79": "parent-emails/session-vaccination-not-given.md",
    "e37fe0a2-7584-4c25-983a-8f5a11c818a1": "parent-emails/session-already-vaccinated.md",
    "ceea5ff5-2250-4eb2-ab35-4e9e840b2a6f": "parent-emails/invitation-to-clinic.md",

    # Text messages to parents
    "c7bd8150-d09e-4607-817d-db75c9a6a966": "parent-messages/consent-request.md",
    "3179b434-4f44-4d47-a8ba-651b58c235fd": "parent-messages/consent-confirm-given.md",
    "eb34f3ab-0c58-4e56-b6b1-2c179270dfc3": "parent-messages/consent-confirm-refused.md",
    "1fd4620d-1c96-4af1-b047-ed13a90b0f44": "parent-messages/consent-unknown-parent-details.md",
    "cc4a7f89-d260-461c-80f0-7e6e9af75e7a": "parent-messages/session-reminder.md",
    "395a3ea1-df07-4dd6-8af1-64cc597ef383": "parent-messages/session-vaccination-given.md",
    "aae061e0-b847-4d4c-a87a-12508f95a302": "parent-messages/session-vaccination-not-given.md",
    "fab1e355-bde1-47d5-835c-103bfd232b93": "parent-messages/session-already-vaccinated.md",
    "790c9c72-729a-40d6-b44d-d480e38f0990": "parent-messages/invitation-to-clinic.md",
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

def strip_square_brackets_and_colons(text: str) -> str:
    return re.sub(r"^\[.*?]\s*", "", text).replace(" (single and multiple vaccines)", "")

def get_file_name(template: dict[str, str|int]) -> str:
    file_name = f"{DEFAULT_TEMPLATE_IDS.get(template.get('id', ''))}"

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
        title = strip_square_brackets_and_colons(template.get("name", ""))
        order = existing_order if existing_order is not None else current_order

        # Build YAML front matter - required fields
        frontmatter = {
            "layout": "email-template" if template.get("type", "email") == "email" else "text-message-template",
            "title": '"' + title + '"',
            "theme": existing_frontmatter.get("theme", None),
            "subject": convert_to_markdown(template.get("subject", ""))
        }

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
