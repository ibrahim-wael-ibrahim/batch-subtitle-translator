for file in *.srt; do
  mv "$file" "${file%.srt}_en.srt"
done
