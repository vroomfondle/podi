{{#originaltitle}}
Title: {{{originaltitle}}} / "{{{title}}}"
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

Episodes:
{{#episodes}}
  {{{episodeid}}}: {{{label}}}
{{/episodes}}
{{^episodes}}
  No episodes.
{{/episodes}}

