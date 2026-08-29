def chunk_text(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> list[str]:

    if not text.strip():
        return []

    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:
        target_end = min(start + chunk_size, text_length)

        if target_end < text_length:
            boundary = text.rfind(" ", start, target_end)

            if boundary > start:
                end = boundary
            else:
                end = target_end
        else:
            end = target_end

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= text_length:
            break

        overlap_start = max(start, end - chunk_overlap)

        # Move the overlap start to a word boundary.
        whitespace = text.find(" ", overlap_start, end)

        if whitespace != -1:
            start = whitespace + 1
        else:
            start = overlap_start

    return chunks