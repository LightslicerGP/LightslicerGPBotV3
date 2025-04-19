# this is to sync the code with the markdown files
import os
import io
import re

root_dir = "commands"

prev_base_name = None
js_exists = md_exists = py_exists = False


def should_insert_before(current: str, inserting: str) -> bool:
    max_len = max(len(current), len(inserting))
    for i in range(max_len):
        c_char = current.lower()[i] if i < len(current) else None
        i_char = inserting.lower()[i] if i < len(inserting) else None

        if c_char is None:
            # current is shorter, like bal gamble vs bal gamble2
            return False
        if i_char is None:
            # inserting is shorter -> comes before current
            return True

        if c_char < i_char:
            return True
        elif c_char > i_char:
            return False

    # If we finish the loop, they are equal
    return False  # default: do not insert before


def process(base_name):
    # print(f"{base_name}: js={js_exists}, md={md_exists}, py={py_exists}")
    if len(base_name.split("\\")) != 3:
        # print("FAILLLLLLLLLLl", base_name)
        return

    if not md_exists or os.path.getsize(f"{base_name}.md") == 0:
        # print(base_name.split("\\")[-1])
        with io.open(f"{base_name}.md", "w", encoding="utf-8") as file:
            with io.open("command.md", "r", encoding="utf-8") as source_file:
                source_content = source_file.read()
                modified_content = source_content.replace(
                    "# #Command", f"# #{base_name.split('\\')[-1].replace("-", " ")}"
                )

                if js_exists:
                    with io.open(f"{base_name}.js", "r", encoding="utf-8") as js_file:
                        js_content = js_file.read()
                    modified_content = modified_content.replace(
                        'console.log("Hello World!")', js_content
                    )

                if py_exists:
                    print("py file exists")
                    with io.open(f"{base_name}.py", "r", encoding="utf-8") as py_file:
                        py_content = py_file.read()
                    modified_content = modified_content.replace(
                        'print("Hello World!")', py_content
                    )
                file.write(modified_content)
    elif md_exists:
        # print("\n----------------------")
        # print(f"{base_name}.md")

        # "economy"
        catagory = base_name.split("\\")[1]
        # "bal-add"
        command = base_name.split("\\")[2]
        # "#bal add"
        command_name = "#" + os.path.basename(base_name).replace("-", " ")
        # "commands/economy/bal-add.md"
        markdown_path = base_name.replace("\\", "/") + ".md"
        # "    * [#bal add](commands/economy/bal-add.md)\n"
        # line_to_insert = f"    * [{command_name}]({markdown_path})\n"
        line_to_insert = f"    * [{command_name}]({markdown_path})\n"

        with io.open("SUMMARY.md", "r", encoding="utf-8") as summary_file:
            lines = summary_file.readlines()

        line_exists = False

        for line in lines:
            if not line_exists:
                if line == line_to_insert:
                    # print("line exists")
                    line_exists = True
                    break

        if not line_exists:
            print("need to insert this line:")
            print(line_to_insert)

        with io.open(f"{base_name}.md", "r", encoding="utf-8") as file:
            content = file.read()

        if js_exists:
            pattern = (
                r'({% code title="AOI\.js" lineNumbers="true" fullWidth="false" %}\n```javascript\n)'
                r"(.*?)"
                r"(\n```[\r]?\n{% endcode %})"
            )

            def insert_code_block(match):
                before = match.group(1)
                code = match.group(2)
                after = match.group(3)

                with io.open(f"{base_name}.js", "r", encoding="utf-8") as js_file:
                    js_content = js_file.read()

                new_code = js_content
                return before + new_code + after

            updated_content = re.sub(
                pattern, insert_code_block, content, flags=re.DOTALL
            )
            content = updated_content

        if py_exists:
            pattern = (
                r'({% code title="Discord\.py" lineNumbers="true" fullWidth="false" %}\n```python\n)'
                r"(.*?)"
                r"(\n```[\r]?\n{% endcode %})"
            )

            def insert_code_block(match):
                before = match.group(1)
                code = match.group(2)
                after = match.group(3)

                with io.open(f"{base_name}.py", "r", encoding="utf-8") as py_file:
                    py_content = py_file.read()

                new_code = py_content
                return before + new_code + after

            updated_content = re.sub(
                pattern, insert_code_block, content, flags=re.DOTALL
            )
            content = updated_content

        with open(f"{base_name}.md", "w", encoding="utf-8") as f:
            f.write(content)


for dirpath, dirnames, filenames in os.walk(root_dir):
    # Skip __pycache__ folders
    dirnames[:] = [d for d in dirnames if d != "__pycache__"]

    # Filter out README.md and sort remaining filenames
    filenames = sorted([f for f in filenames if f != "README.md"])

    for filename in filenames:
        base, ext = os.path.splitext(filename)
        ext = ext.lower()

        current_base_name = os.path.join(dirpath, base)

        if prev_base_name and current_base_name != prev_base_name:
            process(prev_base_name)
            js_exists = md_exists = py_exists = False

        # Set flags based on extension
        if ext == ".js":
            js_exists = True
        elif ext == ".md":
            md_exists = True
        elif ext == ".py":
            py_exists = True

        prev_base_name = current_base_name

# Print the final file's status
if prev_base_name:
    process(prev_base_name)
