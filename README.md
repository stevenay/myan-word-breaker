# Myan-word-breaker
Word segmentation tool for Myanmar sentence.

## Demo
Try this library at [flask-py-word-breaker](https://flask-py-word-breaker.herokuapp.com/)

## Introduction
This is the **word segmentation tool** for Myanmar text. Word segmentation is the process of determining word boundaries in a piece of text.

Word Segmentation is the most basic but very important step for **Natural Language Processing** of Myanmar Text. It is also non-trivial task since Myanmar text is a string of characters without explicit word boundary delimiters.

In this library, the method from the research paper of [Ko Tun Thura Thet (2008) Word segmentation](https://dl.acm.org/citation.cfm?id=1411817) for the Myanmar Language is used.

The library supports two ways to find the possible combinations

 1. All possible combinations loop
 2. Sub-word possibility recursive method.

The first one might be a little bit better to provide more precise result while the later one has huge improvement in runtime performance.

To validate the evaluate these possible combinations, the library uses **Bigram Collocation Strength Statistical Approach** according to described in the research paper.

## Usage

    # coding=utf8
    from word_breaker.word_segment_v5 import WordSegment

    wordSegmenter = WordSegment()
    # Segment using sub_word_possibility segmentation method on Unicode String
    print(wordSegmenter.normalize_break('သဘာဝဟာသဘာဝပါ', 'unicode', wordSegmenter.SegmentationMethod.sub_word_possibility))

    # Segment using sub_word_possibility segmentation method on Zawgyi String
    print(wordSegmenter.normalize_break('သဘာဝဟာသဘာဝပါ', 'zawgyi', wordSegmenter.SegmentationMethod.sub_word_possibility))

    # Segment using all_possible_combination segmentation method on Unicode String
    print(wordSegmenter.normalize_break('သဘာဝဟာသဘာဝပါ', 'unicode', wordSegmenter.SegmentationMethod.all_possible_combination))

    # Segment using all_possible_combination segmentation method on Zawgyi String
    print(wordSegmenter.normalize_break('သဘာဝဟာသဘာဝပါ', 'zawgyi', wordSegmenter.SegmentationMethod.all_possible_combination))

## Todo


 - Create pip package to properly distribute
 - Scoring and evaluate the library precision performance
 - Syllable level separated dictionary files
 - Train Bi-gram Collocation data as a model

## Credit
- [Word segmentation for the Myanmar language](https://dl.acm.org/citation.cfm?id=1411817)
- [MyParser for Syllabification](https://github.com/thantthet/MyanmarParser-Py)
- [Text Corpus from Ko YeKyawThu's myPOS Repo](https://github.com/ye-kyaw-thu/myPOS)
- [Dictionary from MCFNLP](https://github.com/mcfnlp/Head-Word)
- [Stop Words from SwanHtet's Burmese data Repo)(https://github.com/swanhtet1992/myanmar-data)

## License
[MIT](./LICENSE)