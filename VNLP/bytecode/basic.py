def basic(text, line):
    if text.startswith('gán '):
        asign = text[4:]
        parts = asign.split('=',1)
        if len(parts) == 2:
            return f"{line}: ASS {parts[0].strip()} {parts[1].strip()}"
        
    elif text.startswith('viết '):
        pri = text[5:]
        return f"{line}: PRI {pri}"
    