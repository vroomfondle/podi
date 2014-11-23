{{#originaltitle}}
Title: {{originaltitle}} / "{{title}}"
{{/originaltitle}}
{{^originaltitle}}
Title: {{title}}
{{/originaltitle}}

Tagline: {{tagline}}
Air Date: {{firstaired}}
Season: {{season}}

Writers:
{{#writer_dict}}
  {{writer}}
{{/writer_dict}}
{{^writer_dict}}
  No writers available.
{{/writer_dict}}

Cast:
{{#cast}}
  {{role}}: {{name}}
{{/cast}}

Plot:
{{#plot}}
  {{plot}}
{{/plot}}
{{^plot}}
  No plot  available.
{{/plot}}

File: {{file}}
