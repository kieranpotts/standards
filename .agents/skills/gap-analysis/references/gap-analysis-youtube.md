# Extracting a YouTube reference resource

Read this when a reference resource is a YouTube URL, either
`https://www.youtube.com/watch?v=<id>` or `https://youtu.be/<id>`.

The video itself cannot be fetched. YouTube watch pages are JavaScript-rendered,
so a plain web fetch returns page chrome with no video content and no
transcript. Do not report the URL as a simple fetch failure: the creator's
own summary of the video's argument is available without any API key.

## Run the extractor

```sh
python3 .agents/skills/gap-analysis/scripts/gap-analysis/youtube_description.py \
  <video-id-or-url>
```

The argument may be a bare 11-character video id, a watch URL, or a `youtu.be`
short URL. The script reads YouTube's public oEmbed endpoint for the title and
author, and the `ytInitialPlayerResponse` blob embedded in the raw watch-page
HTML for the full description, keywords, and length, then prints them as plain
text. It uses only the Python 3 standard library.

## Use the result

Treat the returned description as the creator's own summary of the video's
thesis and key claims, and compare the standard against that.

Be transparent about the depth of the comparison. Note in the `GAPS.md`
Unresolved section — or alongside any gap the video produces — that the
comparison was against the description and not a full transcript, since claims
made only in the spoken audio could not be verified.

Where the description links to a full transcript hosted elsewhere, as some
creators provide, fetch that transcript and use it as the primary source, with
the description as the fallback.

Where the script fails — the video is private, age-restricted, or removed, or
YouTube has changed its page structure — report that against the resource and
carry on with the rest.
