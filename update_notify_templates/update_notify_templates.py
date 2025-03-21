from notifications_python_client.notifications import NotificationsAPIClient
from dotenv import load_dotenv
import os
import argparse
import re

load_dotenv()

DEFAULT_TEMPLATE_IDS = [
    "6aa04f0d-94c2-4a6b-af97-a7369a12f681",  # Initial consent request for HPV
    "ceefd526-d44c-4561-b0d2-c9ef4ccaba4f",  # First consent reminder for HPV
    "6410145f-dac1-46ba-82f3-a49cad0f66a6",  # Second and beyond reminder for HPV
]


def get_govuk_client() -> NotificationsAPIClient:
    api_key = os.getenv('NOTIFY_API_KEY')
    return NotificationsAPIClient(api_key)


def convert_to_markdown(body: str) -> str:
    # Replace CRLF with LF
    body = body.replace("\r\n", "\n")

    # Replace (((...))) with (==...==)
    body = re.sub(r"\(\(\((.*?)\)\)\)", r"(==\1==)", body)

    # Replace ((...)) with ==...==
    body = re.sub(r"\(\((.*?)\)\)", r"==\1==", body)

    # Replace ^ with > if it's at the start of a line
    body = re.sub(r"^\^", "> ", body, flags=re.MULTILINE)

    return body


def compose_yaml_frontmatter(frontmatter: dict[str, str|int]) -> str:
    yaml_lines = ["---"]
    for key, value in frontmatter.items():
        yaml_lines.append(f"{key}: {value}")
    yaml_lines.append("---\n")
    return "\n".join(yaml_lines)


def strip_square_brackets(text: str) -> str:
    return re.sub(r"^\[.*?]\s*", "", text)


def update_templates(template_ids: list[str], output_dir: str, order_start: int=0) -> None:
    notifications_client = get_govuk_client()

    current_order = order_start

    for template_id in template_ids:
        print(f"Updating template with ID: {template_id}")

        # Get the template from GOV.UK Notify
        template: dict[str, str|int] = notifications_client.get_template(
            template_id=template_id,
        )

        # Build YAML front matter
        frontmatter = {
            "layout": template.get("type", "email"),
            "title": strip_square_brackets(template.get("name", "")),
            "group": "Email templates",
            "subject": convert_to_markdown(template.get("subject", "")),
            "order": current_order,
        }
        yaml_content = compose_yaml_frontmatter(frontmatter)

        # Get and process the body
        body_content = convert_to_markdown(template.get("body", ""))

        # Combine YAML front matter and processed body
        md_content = yaml_content + "\n" + body_content

        # Create output file path
        file_name = f"notify-{template.get("type", "email")}-{strip_square_brackets(template.get("name", "")).lower().replace(" ", "-")}.md"
        output_file = os.path.join(output_dir, file_name)

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
        default="../app/guide"
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
