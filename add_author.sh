#!/bin/bash
# Add author and student ID comment to the top of all project files

COMMENT="# AUTHOR: ALHADJI OUMATE\n# STUDENT ID: 22U2033"

# For Python files
for file in $(find . -type f -name "*.py"); do
    if ! grep -q "AUTHOR: ALHADJI OUMATE" "$file"; then
        sed -i "1i$COMMENT" "$file"
    fi
done

# For Markdown files
for file in $(find . -type f -name "*.md"); do
    if ! grep -q "AUTHOR: ALHADJI OUMATE" "$file"; then
        sed -i "1i<!-- AUTHOR: ALHADJI OUMATE -->\n<!-- STUDENT ID: 22U2033 -->" "$file"
    fi
done

# For YAML/YML files
for file in $(find . -type f \( -name "*.yml" -o -name "*.yaml" \)); do
    if ! grep -q "AUTHOR: ALHADJI OUMATE" "$file"; then
        sed -i "1i# AUTHOR: ALHADJI OUMATE\n# STUDENT ID: 22U2033" "$file"
    fi
done

# For Dockerfile
for file in $(find . -type f -name "Dockerfile"); do
    if ! grep -q "AUTHOR: ALHADJI OUMATE" "$file"; then
        sed -i "1i# AUTHOR: ALHADJI OUMATE\n# STUDENT ID: 22U2033" "$file"
    fi
done

echo "Author and student ID added to all project files."