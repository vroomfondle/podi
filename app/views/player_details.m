Playing {{{type}}}: {{#item}}{{#originaltitle}}{{{originaltitle}}} / {{/originaltitle}}{{{title}}}{{/item}}
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
{{#currentsubtitle}}
  Stream {{{index}}}:
    Name:         {{{name}}}
    Language:     {{{language}}}
{{/currentsubtitle}}

Available subtitle streams:
{{#subtitles}}
  Stream {{{index}}}:
    Name:         {{{name}}}
    Language:     {{{language}}}
{{/subtitles}}
