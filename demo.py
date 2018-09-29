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