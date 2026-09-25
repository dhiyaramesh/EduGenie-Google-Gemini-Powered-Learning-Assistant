import json
import re
from typing import Any

def clean_json_block(json_string: str) -> Any:
    """
    Cleans a JSON string that might be wrapped in Markdown code blocks
    and parses it into a Python object (dict or list).
    """
    # Remove markdown code block syntax if present
    json_string = re.sub(r'```json\n?', '', json_string)
    json_string = re.sub(r'```\n?', '', json_string)
    json_string = json_string.strip()
    
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON: {str(e)}\nRaw string: {json_string}")
