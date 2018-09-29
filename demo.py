# coding=utf8
from word_breaker.word_segment_v5 import WordSegment

wordSegmenter = WordSegment()
print(wordSegmenter.normalize_break('သဘာဝဟာသဘာဝပါ', 'unicode', wordSegmenter.SegmentationMethod.sub_word_possibility))

print(wordSegmenter.normalize_break('သဘာဝဟာသဘာဝပါ', 'zawgyi', wordSegmenter.SegmentationMethod.sub_word_possibility))