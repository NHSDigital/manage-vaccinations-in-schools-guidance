from notifications_python_client.notifications import NotificationsAPIClient
from dotenv import load_dotenv
import os
import argparse
import re

load_dotenv()

DEFAULT_TEMPLATE_IDS = [
    "6aa04f0d-94c2-4a6b-af97-a7369a12f681"
]


def get_all_templates():
    api_key = os.getenv('NOTIFY_API_KEY')
    notifications_client = NotificationsAPIClient(api_key)

    response = notifications_client.get_all_templates()
    return response.get('templates', [])


def filter_templates_by_id(all_templates, template_ids):
    return [template for template in all_templates if template.get('id', '') in template_ids]


def convert_to_markdown(body):
    # Replace ((...??...))

    # Replace (((...))) with (==...==)
    body = re.sub(r"\(\(\((.*?)\)\)\)", r"(==\1==)", body)

    # Replace ((...)) with ==...==
    body = re.sub(r"\(\((.*?)\)\)", r"==\1==", body)

    # Replace ^ with > if it's at the start of a line
    body = re.sub(r"^\^", "> ", body, flags=re.MULTILINE)

    return body


def compose_yaml_frontmatter(frontmatter):
    yaml_lines = ["---"]
    for key, value in frontmatter.items():
        yaml_lines.append(f"{key}: {value}")
    yaml_lines.append("---\n")
    return "\n".join(yaml_lines)


def strip_square_brackets(text):
    return re.sub(r"^\[.*?]\s*", "", text)


def update_templates(template_ids, output_dir, order_start=0):
    all_templates = get_all_templates()
    templates = filter_templates_by_id(all_templates, template_ids)

    current_order = order_start

    for template in templates:
        print(f"Updating template \"{template.get('name', '')}\"...")

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
        file_name = f"notify-email-{strip_square_brackets(template.get("name", "")).lower().replace(" ", "-")}.md"
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
        default=45
    )
    args = parser.parse_args()

    template_ids = args.template_ids.split(',')
    template_ids = [template_id.strip() for template_id in template_ids]

    update_templates(template_ids, args.output_dir, args.order_start)
