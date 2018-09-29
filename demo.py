# coding=utf8
from word_breaker.word_segment_v5 import WordSegment

wordSegmenter = WordSegment()
print(wordSegmenter.normalize_break('အလုပ်မရှိအကိုင်မရှိ၊ လမ်းသွားရင်း ဖုန်းပွတ်၊ လူကြီးသူမနဲ့ စကားပြောနေသလား၊ ဘာလား မဆင်ခြင်နိုင်ဘူး။ လက်မတစ်ခြောင်းနဲ့ ဖေ့စ်ဘုတ်ကို အထက်အောင်ပွတ်နေတာလေးကို ဘဝမှတ်နေတဲ့ စောင်ကလေးတွေ၊ အီးမေးလ်ဝင်စရာမရှိ၊ စီးပွားရေးကိစ္စ၊ လေ့လာစရာ ဘာတစ်ခုမှ မရှိ၊ မဖတ်ပဲ ဖုန်းလေးတစ်လုံးနဲ့ ဘဝကို မြင့်မြတ်နေတဲ့ စောင်ကလေးတွေ လမ်းမှာ တွေ့တွေ့နေရတာ ဇာတ်ပိုးချည်းပဲ အုတ်ပစ်ချင်တာ', 'unicode', wordSegmenter.SegmentationMethod.sub_word_possibility))

print(wordSegmenter.normalize_break('သဘာဝဟာသဘာဝပါ', 'zawgyi', wordSegmenter.SegmentationMethod.sub_word_possibility))