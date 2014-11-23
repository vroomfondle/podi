{{#originaltitle}}
Title: {{originaltitle}} / "{{title}}"
{{/originaltitle}}
{{^originaltitle}}
Title: {{{title}}}
{{/originaltitle}}
Tagline: {{{tagline}}}
Year: {{{year}}}

Genres: 
{{#genre_dict}}
  {{{genre}}}
{{/genre_dict}}
{{^genre_dict}}
  No genres have been set.
{{/genre_dict}}

Tags: 
{{#tag_dict}}
  {{{tag}}}
{{/tag_dict}}
{{^tag_dict}}
  No tags have been set.
{{/tag_dict}}

Writers: 
{{#writer_dict}}
  {{{writer}}}
{{/writer_dict}}
{{^writer_dict}}
  No writers.
{{/writer_dict}}

Cast:
{{#cast}}
  {{{role}}}: {{{name}}}
{{/cast}}

Plot:
{{#plot}}
  {{{plot}}}
{{/plot}}
{{^plot}}
  No plot  available.
{{/plot}}

File: {{{file}}}

