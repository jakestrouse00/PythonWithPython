from __future__ import annotations
import re

__all__ = ["tab_spacing", "remove_forward_ref"]

tab_spacing = "    "

def remove_forward_ref(input_string):
    # Regular expression pattern to match ForwardRef('...') but capture only the content inside the quotes
    pattern = r"ForwardRef\('(.*?)'\)"

    # Replace ForwardRef('...') with the content inside the quotes
    cleaned_string = re.sub(pattern, r'\1', input_string)

    return cleaned_string