def is_image_only(
        pdf,
        *,
        min_page_text_chars: int = 20,
        min_doc_text_chars: int = 200,
        threshold: float = 0.8,
) -> bool:
    """
    Classify a PDF as "image-only" (scanned) if:
      - Most non-empty pages contain images, AND
      - Most non-empty pages have very little extractable text, AND
      - Total extractable text across the doc is low.

    Important: A digital PDF can have small text and still be valid.
    So we require images to be present on most pages before rejecting.
    """

    checked_pages = 0
    low_text_pages = 0
    image_pages = 0
    total_text_chars = 0

    for page in pdf.pages:
        text = (page.extract_text() or "").strip()
        text_len = len(text)
        imgs = getattr(page, "images", []) or []
        has_images = len(imgs) > 0

        # Skip truly empty pages (no text and no images)
        if text_len == 0 and not has_images:
            continue

        checked_pages += 1
        total_text_chars += text_len

        if has_images:
            image_pages += 1

        if text_len < min_page_text_chars:
            low_text_pages += 1

    if checked_pages == 0:
        return False

    # If there are basically no images, it's not a scanned/image-only PDF
    if image_pages == 0:
        return False

    ratio_low_text = low_text_pages / checked_pages
    ratio_images = image_pages / checked_pages

    return (
            total_text_chars < min_doc_text_chars
            and ratio_low_text >= threshold
            and ratio_images >= threshold
    )
