# ai_shell/safety.py
def is_safe_command(command):
    dangerous = ['rm -rf', ':(){:|:&};:', 'mkfs', 'dd if=']
    return not any(d in command for d in dangerous)
