# coding=utf8
from word_breaker.word_segment_v5 import WordSegment

wordSegmenter = WordSegment()
print(wordSegmenter.normalize_break(' ဆိုပြီး စိတ်ကူးထားတဲ့ မင်္ဂလာပွဲပုံစံကို ပြောပြလာတဲ့ ဝါဆိုမိုးဦး', 'unicode', wordSegmenter.SegmentationMethod.sub_word_possibility))


