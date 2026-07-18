import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:

        absolute_path = os.path.abspath(working_directory)

        target_dir = os.path.normpath(os.path.join(absolute_path, file_path))

        valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path

        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
    
        #we make sure that the parent directories exist
        #by running this function which does nothing if they already
        #exist or just create them
        os.makedirs(os.path.dirname(target_dir), exist_ok=True)

        with open(target_dir, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
       return f"Error: {e}"
    
schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes to file and creates parent directory if not already available",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "path to file to be written to",
                    }, 
                "content": {
                    "type": "string",
                    "description": "content to be written into file"
                }
            },
            "required": ["file_path","content"]
        },
    },
}