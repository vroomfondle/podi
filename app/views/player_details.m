Playing {{{type}}}
{{#totaltime}}
Length: {{{hours}}}:{{{minutes}}}:{{{seconds}}}
{{/totaltime}}
{{#time}}
Current position: {{{hours}}}:{{{minutes}}}:{{{seconds}}}
{{/time}}
Repeat?: {{#repeat}}Yes{{/repeat}}{{^repeat}}No{{/repeat}}

Current audio stream:
{{#currentaudiostream}}
  Name:         {{{name}}}
  Language:     {{{language}}}
  Channels:     {{{channels}}}
  Codec:        {{{codec}}}
{{/currentaudiostream}}

Available audio streams:
{{#audiostreams}}
  Stream {{{index}}}:
    Language:     {{{language}}}
    Channels:     {{{channels}}}
    Codec:        {{{codec}}}
{{/audiostreams}}

Current subtitle stream:
{{#currentsubtitles}}
  Name:         {{{name}}}
  Language:     {{{language}}}
{{/currentsubtitles}}

Available subtitle streams:
{{#subtitles}}
  Stream {{{index}}}:
    Name:         {{{name}}}
    Language:     {{{language}}}
{{/subtitles}}
