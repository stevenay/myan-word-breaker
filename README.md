Myan-word-breaker
Word segmentation tool for Myanmar sentence.

Demo
flask-py-word-breaker.herokuapp.com

Introduction
This is the word segmentation tool for Myanmar text. Word segmentation is the process of determining word boundaries in a piece of text.
Word Segmentation is the most basic but very important step for Natural Language Processing of Myanmar Text. It is also non-trivial task since Myanmar text is a string of characters without explicit word boundary delimiters.
In this library, I use the method from the research paper of Ko Tun Thura Thet (2008) Word segmentation for the Myanmar Language. There is two phases in this method: syllable segmentation and syllable merging. A rule-based heuristic approach was adopted for syllable segmentation, and a dictionary-based statistical approach for syllable merging.
