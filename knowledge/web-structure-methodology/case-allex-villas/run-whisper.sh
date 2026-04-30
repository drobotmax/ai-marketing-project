#!/bin/bash
set -e
cd "$(dirname "$0")"
START=$(date +%s)
for f in raw/audio/*.mp3; do
  base=$(basename "$f" .mp3)
  out="transcripts/${base}.txt"
  if [ -f "$out" ]; then
    echo "[skip] $base already transcribed"
    continue
  fi
  echo "[$(date +%H:%M:%S)] transcribing $base..."
  whisper "$f" \
    --model turbo \
    --language Russian \
    --output_dir transcripts \
    --output_format txt \
    --verbose False \
    >> logs/whisper.log 2>&1
done
END=$(date +%s)
echo "Done. Total: $((($END-$START)/60)) min" >> logs/whisper.log
