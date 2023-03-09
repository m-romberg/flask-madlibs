"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, ...):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, name, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text
        self.name = name

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

silly_story = Story("silly",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time, in a long-ago {place}, there lived an exceptionally
       {adjective} {noun}. It loved to {verb} with {plural_noun}."""
)

# Here's another --- you should be able to swap in app.py to use this story,
# and everything should still work

excited_story = Story("excited",
    ["noun", "verb"],
    """OMG!! OMG!! I love to {verb} a {noun}!"""
)

sad_story = Story("sad",
    ["place", "noun"],
    """I went to {place} yesterday and saw a {noun} crying."""
)
stories = {story.name: story for story in [silly_story, excited_story, sad_story] }
