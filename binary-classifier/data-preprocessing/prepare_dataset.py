import pandas as pd
import numpy as np
import json
import os

anik_samples = [
    {
        "bangla": "আমাদের কালকের ক্লাস টেস্ট নিয়ে কেউ চিন্তা করছে না, কিন্তু আমি বেশ টেনশন করছি।",
        "english": "No one is worried about tomorrow's class test, but I am quite stressed.",
        "banglish": "Amader kalker class test niye keu chinta korche na, kintu ami besh tension korchi."
    },
    {
        "bangla": "ফুটবল ম্যাচে আমাদের দলের অধিনায়ক ইনজুরড, কালকে ম্যাচে কি হবে জানি না।",
        "english": "Our team's captain is injured in the football match, I don't know what will happen tomorrow.",
        "banglish": "Football match e amader dal er odhinayok injured, kalke match e ki hobe jani na."
    },
    {
        "bangla": "ক্লাস টেস্টের পেপার তো এখনো জমা দেওয়া হয়নি, সবাই দেরি করতেছে।",
        "english": "The class test paper hasn’t been submitted yet, everyone is delaying.",
        "banglish": "Class test er paper to ekhono joma deya hoyni, shobai deri kortese."
    },
    {
        "bangla": "আশেপাশের হাসপাতালের অবস্থা বেশ খারাপ শুনলাম।",
        "english": "I heard the condition of nearby hospitals is quite bad.",
        "banglish": "Ashepasher hospital er obostha besh kharap shunlam."
    },
    {
        "bangla": "আমার রক্তের গ্রুপ A+, কিন্তু রক্তদান করার মত পরিস্থিতি নেই এখন।",
        "english": "My blood group is A+, but there's no situation to donate blood right now.",
        "banglish": "Amar rokter group A+, kintu roktodan korar moto poristhiti nei ekhono."
    },
    {
        "bangla": "প্রোগ্রামিং প্রতিযোগিতার ডেডলাইন দাড়িয়েছে, সবাই প্রস্তুতি নিচ্ছে।",
        "english": "The deadline for the programming competition is nearing, everyone is preparing.",
        "banglish": "Programming protijogitar deadline dariyeche, shobai prostuti nitese."
    },
    {
        "bangla": "মিরপুরে একটা বড় দুর্ঘটনা ঘটেছে, অনেক মানুষ আহত।",
        "english": "A big accident happened in Mirpur, many people are injured.",
        "banglish": "Mirpure ekta boro durghotona ghoteche, onek manush ahoto."
    },
    {
        "bangla": "এবারের পিকনিকে আমরা কক্সবাজারে যাচ্ছি, অসাধারণ মজা হবে।",
        "english": "We're going to Cox's Bazar for this year's picnic, it's going to be amazing.",
        "banglish": "Ebarer picnic e amra Cox's Bazar e jacchi, osadharon moja hobe."
    },
    {
        "bangla": "ব্লাড গ্রুপ জানার দরকার নেই, সবাই একসাথে কাজ করতে পারলেই ভালো হয়।",
        "english": "There's no need to know the blood group, it’s better if everyone can work together.",
        "banglish": "Blood group janar dorkar nei, shobai eksathe kaj korte parle bhalo hoy."
    },
    {
        "bangla": "ম্যাচের অবস্থা একদমই ভালো না, সবাই ইমারজেন্সি মিটিং ডাকছে।",
        "english": "The match situation is really bad, everyone is calling for an emergency meeting.",
        "banglish": "Match er obostha ekdomi bhalo na, shobai emergency meeting dakche."
    },
    {
        "bangla": "ক্যাম্পাসের বাইরে নতুন রেস্টুরেন্ট খুলেছে, মেন্যুতে চমৎকার সব খাবার আছে।",
        "english": "A new restaurant has opened outside campus, the menu has amazing food.",
        "banglish": "Campus er baire notun restaurant khulese, menu te chomotkar shob khabar ase."
    },
    {
        "bangla": "মুভি নাইট প্ল্যান করেছিলাম, কিন্তু সবাই ইনজুরড মনে হচ্ছে।",
        "english": "We planned a movie night, but it seems like everyone is injured.",
        "banglish": "Movie night plan korechilam, kintu shobai injured mone hochhe."
    },
    {
        "bangla": "আগামী সপ্তাহে রেজাল্ট বের হবে, দোয়া করো সবাই যেন ভালো করি।",
        "english": "Results will be out next week, pray that everyone does well.",
        "banglish": "Agami shoptah e result ber hobe, doa koro shobai jeno bhalo kori."
    },
    {
        "bangla": "সোশ্যাল মিডিয়ায় রোগীর অবস্থা নিয়ে অনেক গুজব ছড়াচ্ছে, বিশ্বাস করো না।",
        "english": "There are many rumors spreading about the patient's condition on social media, don’t believe them.",
        "banglish": "Social media te rogir obostha niye onek gujob chhorachhe, bishash koro na."
    },
    {
        "bangla": "এটা রক্তের ব্যাগ নয়, এটা তো একেবারে ভুল ধারণা।",
        "english": "This is not a blood bag, this is a completely wrong idea.",
        "banglish": "Eta rokter bag noy, eta to ekebare bhul dharana."
    },
    {
        "bangla": "আমাদের ক্যাম্পাসের হেলথ ক্যাম্পে এবার ইমারজেন্সি কিট থাকবে।",
        "english": "This time the campus health camp will have emergency kits.",
        "banglish": "Amader campus er health camp e eibar emergency kit thakbe."
    },
    {
        "bangla": "অনুষ্ঠানের জন্য সবাই প্রস্তুতি নিচ্ছে, কিন্তু কেউই রক্তদান নিয়ে কথা বলছে না।",
        "english": "Everyone is preparing for the event, but no one is talking about blood donation.",
        "banglish": "Onusthan er jonne shobai prostuti nitese, kintu keu roktodan niye kotha bolchhe na."
    },
    {
        "bangla": "ট্যুরের প্ল্যান শেষ, এবার শুধু টিকিটের ব্যবস্থা করতে হবে।",
        "english": "The tour plan is done, now we just need to arrange the tickets.",
        "banglish": "Tour er plan sesh, ebar shudhu ticket er byabostha korte hobe."
    },
    {
        "bangla": "ইনজুরির পর সাকিবকে নিয়ে অনেক সন্দেহ ছিল, কিন্তু ও দারুণভাবে কামব্যাক করেছে।",
        "english": "There were many doubts about Shakib after the injury, but he made a great comeback.",
        "banglish": "Injury er por Shakib ke niye onek shondeho chhilo, kintu o darun vabe comeback koreche."
    },
    {
        "bangla": "সিনিয়র ভাইয়ার ল্যাব ক্লাস অনেক কঠিন, সবাই খুবই ভয়ে থাকে।",
        "english": "Senior brother's lab class is really tough, everyone is quite scared.",
        "banglish": "Senior bhai er lab class onek kothin, shobai khub bhoy e thake."
    },
    {
        "bangla": "কক্সবাজারের এই ছবি দেখে মনটা ভালো হয়ে গেল।",
        "english": "Seeing this picture of Cox's Bazar really lifted my mood.",
        "banglish": "Cox's Bazar er ei chhobi dekhe mon ta bhalo hoye gelo."
    },
    {
        "bangla": "এবারের ক্রিকেট ম্যাচে আমাদের দল খুবই দুর্বল খেললো, সিনিয়র প্লেয়ার সবাই আহত।",
        "english": "Our team played very poorly in the cricket match this time, all the senior players are injured.",
        "banglish": "Ebarer cricket match e amader dal khub durbol khello, senior player shobai ahoto."
    },
    {
        "bangla": "ক্যাম্পাসের পলিটিক্স নিয়ে কথা না বলাই ভালো, সবাই নিজেদের চিন্তায় ব্যস্ত।",
        "english": "It's better not to talk about campus politics, everyone is busy with their own thoughts.",
        "banglish": "Campus er politics niye kotha na bolai bhalo, shobai nijeder chinta te byasto."
    },
    {
        "bangla": "ফাইনাল পরীক্ষার রুটিন বের হয়েছে, আর মাত্র কয়েক দিন বাকি।",
        "english": "The final exam schedule is out, only a few days left.",
        "banglish": "Final porikkhar routine ber hoyeche, ar matro koyek din baki."
    },
    {
        "bangla": "ইনজেকশনের ভয়ে কেউ ব্লাড টেস্ট করতে চায় না।",
        "english": "No one wants to do a blood test out of fear of injections.",
        "banglish": "Injection er bhoye keu blood test korte chai na."
    },
    {
        "bangla": "আগামীকাল এসাইনমেন্ট জমা দেওয়ার শেষ দিন, কেউ যেন দেরি না করে।",
        "english": "Tomorrow is the last day to submit the assignment, no one should be late.",
        "banglish": "Agamikal assignment joma dewar shesh din, keu jeno deri na kore."
    },
    {
        "bangla": "পিকনিকে আমাদের গাইড ঠিক করেছে, সবাই নিজে খেয়াল রাখিস।",
        "english": "We have fixed our guide for the picnic, everyone take care of yourselves.",
        "banglish": "Picnic e amader guide thik koreche, shobai nije khyal rakhish."
    },
    {
        "bangla": "এত চাপের মধ্যে কেউ ভালো করতে পারছে না, মনে হয় কেউ আহত না হয়েই খুশি থাকা উচিত।",
        "english": "No one is able to perform well under this pressure, it seems we should be happy if no one gets injured.",
        "banglish": "Eto chap er modhye keu bhalo korte parche na, mone hoy keu ahoto na hoy e khushi thaka uchit."
    },
    {
        "bangla": "ফুটবলের প্র্যাকটিসের জন্য স্টেডিয়ামে গিয়ে দেখি সবাই ইমারজেন্সি চিকিৎসা নিচ্ছে।",
        "english": "Went to the stadium for football practice and saw everyone getting emergency treatment.",
        "banglish": "Football er practice er jonno stadium e giye dekhi shobai emergency chikitsa nitese."
    },
    {
        "bangla": "মিউজিক ক্লাবে নতুন সদস্য নিয়োগ চলছে, সবাই যোগ দিতে পারো।",
        "english": "The music club is recruiting new members, everyone can join.",
        "banglish": "Music club e notun sadosh niyog cholche, shobai jog dite paro."
    },
    {
        "bangla": "ডেডলাইন কাছে আসছে, প্রজেক্টে রক্ত পানি করে কাজ করতে হচ্ছে।",
        "english": "The deadline is approaching, we're working tirelessly on the project.",
        "banglish": "Deadline kachhe ashche, project e rokt pani kore kaj korte hocche."
    },
    {
        "bangla": "সিনেমা দেখার প্ল্যান করলাম, কিন্তু কেউই সময় দিতে পারছে না।",
        "english": "We planned to watch a movie, but no one has time.",
        "banglish": "Cinema dekhar plan korlam, kintu keu somoy dite parche na."
    },
    {
        "bangla": "এবারের হ্যাকাথনে অংশগ্রহণ করা দলগুলো অনেক ভালো করছে।",
        "english": "The teams participating in this year’s hackathon are doing really well.",
        "banglish": "Ebarer hackathon e onshogrohon kora dalgulo onek bhalo korche."
    },
    {
        "bangla": "ক্লাস টেস্টের পর সবাই একটু হালকা মুডে আছে, মজার মজার মেমে শেয়ার করছে।",
        "english": "Everyone is in a light mood after the class test, sharing funny memes.",
        "banglish": "Class test er por shobai ektu halka mood e ache, moja moja meme share korche."
    },
    {
        "bangla": "আশেপাশের হাসপাতালে নতুন মেডিকেল ক্যাম্প চলছে, চাইলে ঘুরে আসতে পারো।",
        "english": "A new medical camp is going on at nearby hospitals, you can visit if you want.",
        "banglish": "Ashepasher hospital e notun medical camp cholche, chaile ghure aste paro."
    },
    {
        "bangla": "ট্যুর প্ল্যানিং নিয়ে সবাই বেশ উত্তেজিত, কিন্তু বাস ঠিক করা এখনো হয়নি।",
        "english": "Everyone is excited about the tour planning, but the bus hasn't been finalized yet.",
        "banglish": "Tour planning niye shobai besh uttejito, kintu bus thik kora ekhono hoyni."
    },
    {
        "bangla": "ইংলিশ প্রেজেন্টেশনের স্লাইড বানানো শুরু করেছি, কিন্তু শেষ করতে পারছি না।",
        "english": "I have started making the slides for the English presentation, but can't finish them.",
        "banglish": "English presentation er slide banano shuru korechi, kintu shesh korte parchi na."
    },
    {
        "bangla": "সিনিয়র ভাইয়ের কাছ থেকে ক্লাস নোট নিয়েছি, অনেক হেল্পফুল হয়েছে।",
        "english": "I got the class notes from the senior brother, they've been very helpful.",
        "banglish": "Senior bhai er kach theke class note niyechi, onek helpful hoyeche."
    },
    {
        "bangla": "আজকের ইভেন্টে সবাই অংশগ্রহণ করুক, মজা হবে।",
        "english": "Everyone should participate in today’s event, it’s going to be fun.",
        "banglish": "Ajker event e shobai onshogrohon korun, moja hobe."
    },
    {
        "bangla": "ক্যাম্পাসের রাস্তাগুলোতে অনেক বেশি যানজট, সবার আসতে দেরি হচ্ছে।",
        "english": "There’s a lot of traffic on the campus roads, everyone is getting delayed.",
        "banglish": "Campus er rastagulo te onek beshi janjot, shobar aste deri hocche."
    },
    {
        "bangla": "প্রেডিকশন ছিল আমাদের দল জিতবে, কিন্তু শেষ মুহূর্তে হেরে গেল।",
        "english": "The prediction was that our team would win, but they lost at the last moment.",
        "banglish": "Prediction chhilo amader dal jitbe, kintu shesh muhurte here gelo."
    },
    {
        "bangla": "অ্যাসাইনমেন্টে ভুল হয়েছে, টিচার আবার জমা দিতে বলেছে।",
        "english": "There were mistakes in the assignment, the teacher has asked to resubmit.",
        "banglish": "Assignment e bhul hoyeche, teacher abar joma dite bolese."
    },
    {
        "bangla": "পলিটিক্স নিয়ে এতো ঝামেলা চলছে, সবাই চিন্তিত।",
        "english": "There is so much trouble going on with politics, everyone is worried.",
        "banglish": "Politics niye eto jhamela cholche, shobai chintito."
    },
    {
        "bangla": "সবার প্রজেক্ট জমা দেওয়ার শেষ দিন কালকে, কোনো ভুল করা যাবে না।",
        "english": "Tomorrow is the last day to submit everyone’s project, no mistakes can be made.",
        "banglish": "Shobar project joma dewar shesh din kalkhe, kono bhul kora jabe na."
    },
    {
        "bangla": "শুনেছি ক্যাম্পাসের ইনজুরড ছাত্ররা সবাই সুস্থ হয়ে গেছে।",
        "english": "I heard that all the injured students on campus have recovered.",
        "banglish": "Shunechi campus er injured chatro ra shobai shustho hoye geche."
    },
    {
        "bangla": "এইবারের হ্যাকাথনের ডেডলাইন আরো কঠিন, সবাই প্রচুর কষ্ট করছে।",
        "english": "The deadline for this year’s hackathon is even tougher, everyone is working really hard.",
        "banglish": "Eibarer hackathon er deadline aro kothin, shobai prochur koshto korche."
    },
    {
        "bangla": "ব্লাড ব্যাংকে কোনো কাজ নেই, সবাই মিথ্যা তথ্য ছড়াচ্ছে।",
        "english": "There’s no work at the blood bank, everyone is spreading false information.",
        "banglish": "Blood bank e kono kaj nei, shobai mittha totho chhoriyeche."
    },
    {
        "bangla": "এইবারের পরীক্ষায় সবার পারফরম্যান্স দেখে মনে হচ্ছে সবাই ভালো করবে।",
        "english": "Looking at everyone’s performance in this exam, it seems everyone will do well.",
        "banglish": "Eibarer porikkhay shobar performance dekhe mone hochhe shobai bhalo korbe."
    },
    {
        "bangla": "ক্যাম্পাসের নতুন ব্লাড গ্রুপ ডোনেশন ইভেন্টের আয়োজন করা হচ্ছে, তবে সেটা নিয়ে বেশি কথা বলছে না।",
        "english": "A new blood group donation event is being organized on campus, but people aren’t talking much about it.",
        "banglish": "Campus er notun blood group donation event er ayojon kora hocche, tobe seta niye beshi kotha bolche na."
    },
    {
        "bangla": "আমাদের সেমিস্টারের পড়াশোনা শেষের দিকে, এক্সাম নিয়ে অনেক টেনশন হচ্ছে।",
        "english": "Our semester's studies are coming to an end, and there’s a lot of tension regarding exams.",
        "banglish": "Amader semester er porashona shesh er dike, exam niye onek tension hochhe."
    },
    {
        "bangla": "পলিটিক্সের আলোচনা নিয়ে ক্যাম্পাসে এত আলোচনা, কিন্তু কেউ সঠিক তথ্য জানে না।",
        "english": "There is so much discussion about politics on campus, but no one knows the correct information.",
        "banglish": "Politics er alochona niye campus e eto alochona, kintu keu thik totho jane na."
    },
    {
        "bangla": "একটা ব্লাড ডোনেশন নিয়ে মিথ্যা প্রচারণা শুরু হয়েছে, সবাই সাবধান থাকিস।",
        "english": "A false campaign has started about blood donation, everyone stay alert.",
        "banglish": "Ekta blood donation niye mittha procharona shuru hoyeche, shobai shabdhan thakish."
    },
    {
        "bangla": "আগামী সপ্তাহে ফুটবল টুর্নামেন্ট আছে, সবাই সময় মতো পৌঁছাবি। আহত হলে প্র্যাকটিস বাদ দিস।",
        "english": "The football tournament is next week, make sure to arrive on time. Skip practice if you’re injured.",
        "banglish": "Agami shoptah e football tournament ache, shobai somoy moto pouchhabi. Ahoto hole practice bad dis."
    },
    {
        "bangla": "পলিটিক্সের ক্লাসে এত বেশি চাপ! বুঝতেই পারছি না কীভাবে পড়ব।",
        "english": "There’s so much pressure in the politics class! I don’t even know how to study.",
        "banglish": "Politics er class e eto beshi chap! Bujhtei parchi na kivabe porbo."
    },
    {
        "bangla": "ক্যাম্পাসে আজকে মুভি স্ক্রিনিং ছিল, কিন্তু কেউ আসলো না! একা একা মুভি দেখলাম।",
        "english": "There was a movie screening on campus today, but no one came! I watched the movie alone.",
        "banglish": "Campus e ajke movie screening chhilo, kintu keu aslo na! Eka eka movie deklam."
    },
    {
        "bangla": "ইউনিভার্সিটির পিকনিকের জন্য এখনো বাস বুক করা হয়নি। দেরি হলে সবাই রাগ করবে।",
        "english": "The bus for the university picnic hasn’t been booked yet. Everyone will be mad if it’s delayed.",
        "banglish": "University er picnic er jonno ekhono bus book kora hoyni. Deri hole shobai rag korbe."
    },
    {
        "bangla": "আমাদের টিমের প্রোগ্রামিং প্রতিযোগিতার ডেডলাইন পেরিয়ে যাচ্ছে, কেউ মনোযোগ দিচ্ছে না।",
        "english": "Our team's programming competition deadline is approaching, but no one is focusing.",
        "banglish": "Amader team er programming protijogita er deadline pere jachhe, keu monojog dichhe na."
    },
    {
        "bangla": "এই সেমিস্টারের ক্লাস টেস্টগুলো খুব কঠিন ছিল, মনে হচ্ছে সবাই খারাপ করেছে।",
        "english": "This semester's class tests were really tough, it seems like everyone did poorly.",
        "banglish": "Ei semester er class test gulo khub kothin chhilo, mone hochhe shobai kharap koreche."
    },
    {
        "bangla": "আজকে মিউজিক ক্লাবে নতুন একজন মেম্বার যোগ দিয়েছে, খুব ভালো গায়ক।",
        "english": "A new member joined the music club today, a very good singer.",
        "banglish": "Ajke music club e notun ekjon member jog diyeche, khub bhalo gayok."
    },
    {
        "bangla": "এসাইনমেন্টের ডেডলাইন আরো এক সপ্তাহ বাড়িয়েছে, তাই একটু দেরি করে জমা দিলেও হবে।",
        "english": "The assignment deadline has been extended by another week, so it's okay to submit a bit late.",
        "banglish": "Assignment er deadline aro ek shoptah barieche, tai ektu deri kore joma dileo hobe."
    },
    {
        "bangla": "সিনিয়র ভাইয়ের কাছ থেকে অ্যাসাইনমেন্টে হেল্প নিচ্ছি, কিন্তু ক্লাসে উপস্থাপনা কেমন হবে জানি না।",
        "english": "I’m getting help from a senior brother for the assignment, but I don’t know how the class presentation will go.",
        "banglish": "Senior bhai er kach theke assignment e help nichhi, kintu class e uposthapona kemon hobe jani na."
    },
    {
        "bangla": "নেক্সট ট্যুর প্ল্যানিং নিয়ে সবাই এত উত্তেজিত, কিন্তু বাজেট নিয়ে আলোচনা করছে না।",
        "english": "Everyone is so excited about the next tour planning, but no one is discussing the budget.",
        "banglish": "Next tour planning niye shobai eto uttejito, kintu budget niye alochona korche na."
    },
    {
        "bangla": "আমাদের মেমের গ্রুপে নতুন মজার পোস্টগুলো দেখে হাসি থামছেই না!",
        "english": "The new funny posts in our meme group are making me laugh nonstop!",
        "banglish": "Amader meme group e notun moja moja post gulo dekhe hashi thamchei na!"
    },
    {
        "bangla": "এইবারের টুর্নামেন্টে আমাদের সিনিয়র প্লেয়ার সবাই ভালো করেছে।",
        "english": "All our senior players performed well in this tournament.",
        "banglish": "Eibarer tournament e amader senior player shobai bhalo koreche."
    },
    {
        "bangla": "ফেসবুকে আজকের ক্যাম্পাসের প্রোটেস্টের ছবি দেখে মনে হচ্ছে সবাই অংশগ্রহণ করেছে।",
        "english": "Seeing the pictures of today’s campus protest on Facebook, it seems like everyone participated.",
        "banglish": "Facebook e ajker campus er protest er chhobi dekhe mone hochhe shobai onshogrohon koreche."
    },
    {
        "bangla": "এই সেমিস্টারে এত বেশি টাস্ক দিয়েছে, মনে হচ্ছে ক্যাম্পাসে আর সময় কাটানো যাবে না।",
        "english": "They have given so many tasks this semester, it feels like there will be no time to hang out on campus.",
        "banglish": "Ei semester e eto beshi task diyeche, mone hochhe campus e ar somoy katano jabe na."
    },
    {
        "bangla": "ব্লাড ডোনেশন ক্যাম্প নিয়ে এত আলোচনা হচ্ছে, কিন্তু কেউ শিউর নয়।",
        "english": "There’s so much discussion about the blood donation camp, but no one is sure.",
        "banglish": "Blood donation camp niye eto alochona hochhe, kintu keu shure noi."
    },
    {
        "bangla": "আমাদের স্যারদের কাছে প্রেজেন্টেশন জমা দিতে হবে আজকে, আর কোনো এক্সকিউজ চলবে না।",
        "english": "We have to submit the presentation to our teachers today, no more excuses will work.",
        "banglish": "Amader sir der kachhe presentation joma dite hobe ajke, ar kono excuse cholbe na."
    },
    {
        "bangla": "আমাদের এই ক্যাম্পাসের সমস্যা নিয়ে আজকে অনেক আলোচনা হল, কিন্তু সল্যুশন পাওয়া যায়নি।",
        "english": "There was a lot of discussion about the problems of our campus today, but no solution was found.",
        "banglish": "Amader ei campus er shomoshya niye ajke onek alochona holo, kintu solution paowa jaini."
    },
    {
        "bangla": "মুভি দেখার পরিকল্পনা করলাম, কিন্তু সবাই ব্যস্ত হয়ে গেল।",
        "english": "We planned to watch a movie, but everyone got busy.",
        "banglish": "Movie dekhar porikolpona korlam, kintu shobai byasto hoye gelo."
    },
    {
        "bangla": "এই মিউজিক ফেস্টিভ্যালে নতুন কিছু ব্যান্ড পারফর্ম করতে যাচ্ছে, মিস করা উচিত হবে না।",
        "english": "Some new bands are going to perform at this music festival, it shouldn't be missed.",
        "banglish": "Ei music festival e notun kichu band perform korte jachhe, miss kora uchit hobe na."
    },
    {
        "bangla": "আমাদের গ্রুপ প্রোজেক্টে এখনো ফাইনাল টাচ বাকি, কিন্তু সবাই অলস।",
        "english": "The final touch on our group project is still pending, but everyone is lazy.",
        "banglish": "Amader group project e ekhono final touch baki, kintu shobai alosh."
    },
    {
        "bangla": "এই সেমিস্টারের ডেডলাইন এত বেশি যে সবাই মানসিকভাবে ডিপ্রেসড হয়ে গেছে।",
        "english": "The deadlines this semester are so intense that everyone has become mentally depressed.",
        "banglish": "Ei semester er deadline eto beshi je shobai manoshikvabe depressed hoye geche."
    },
    {
        "bangla": "নেক্সট ইভেন্টে অংশগ্রহণ করতে পারবো না, কারণ আমার মেডিকেল চেকআপ আছে।",
        "english": "I won't be able to participate in the next event because I have a medical checkup.",
        "banglish": "Next event e onshogrohon korte parbo na, karon amar medical checkup ache."
    },
    {
        "bangla": "আমাদের ক্যাম্পাসের পলিটিকাল ইভেন্টগুলো নিয়ে বেশ বিতর্ক চলছে।",
        "english": "There’s a lot of debate going on about the political events on our campus.",
        "banglish": "Amader campus er political event gulo niye besh bitorko cholche."
    },
    {
        "bangla": "এবারের ট্যুরে কোথায় যাচ্ছি সেটা ঠিক হয়নি এখনো।",
        "english": "It hasn’t been decided where we’re going on this tour yet.",
        "banglish": "Ebarer tour e kothay jachhi seta thik hoyni ekhono."
    },
    {
        "bangla": "ফিজিক্সের ক্লাসে আমাদের নতুন প্রফেসর সবার চোখে পড়েছে, কিন্তু উনার স্বাস্থ্য ঠিক নেই।",
        "english": "Our new physics professor has caught everyone's eye, but their health is not great.",
        "banglish": "Physics er class e amader notun professor shobar chokhe porse, kintu unar shastho thik nei."
    },
    {
        "bangla": "কেমিস্ট্রি পরীক্ষায় ব্লাড গ্রুপ নিয়ে প্রশ্ন এসেছে, কিন্তু আমি সেই বিষয়ে পড়িনি।",
        "english": "In the chemistry exam, a question about blood groups came up, but I haven't studied that topic.",
        "banglish": "Chemistry porikkhay blood group niye proshno esheche, kintu ami shei bishoye porhini."
    },
    {
        "bangla": "গণিতের সমস্যা সমাধানে নতুন টেকনিক আবিষ্কৃত হয়েছে, তবে অনেকেই এখনো জানে না।",
        "english": "A new technique has been discovered for solving math problems, but many still don't know about it.",
        "banglish": "Goniter shomossha somadhane notun technique abiskar hoyeche, kintu onekei ekhono jane na."
    },
    {
        "bangla": "আইটি ফিল্ডে কাজ করতে হলে অনেক সমস্যার সম্মুখীন হতে হয়, বিশেষ করে কোডিং এরর নিয়ে।",
        "english": "Working in the IT field involves facing many challenges, especially with coding errors.",
        "banglish": "IT field e kaj korte hole onek shomoshyar shomukhine hote hoy, bishesh kore coding error niye."
    },
    {
        "bangla": "বিগ টেক কোম্পানির বেতন নিয়ে আলোচনা চলছে, কিন্তু সঠিক তথ্য নেই।",
        "english": "There’s a discussion going on about salaries at big tech companies, but no accurate information.",
        "banglish": "Big tech company er beton niye alochona cholche, kintu shothik totho nei."
    },
    {
        "bangla": "এলএলএম টেকনোলজির ভবিষ্যৎ নিয়ে সবাই আলোচনা করছে, কিন্তু সমাধানের দিকে কেউ যাচ্ছে না।",
        "english": "Everyone is discussing the future of LLM technology, but no one is heading towards solutions.",
        "banglish": "LLM technology er bhobishwot niye shobai alochona korche, kintu keu somadhaner dike jachche na."
    },
    {
        "bangla": "টেক সেলিব্রিটিদের নিয়ে আলোচনা চলছে, কিন্তু কাউকে আসলে বিশ্বাস করা যায় না।",
        "english": "There’s a discussion about tech celebrities, but no one can truly be trusted.",
        "banglish": "Tech celebrities niye alochona cholche, kintu keu asole biswas kora jayna."
    },
    {
        "bangla": "পিসি এরর সমাধানে সবাই চেষ্টা করছে, কিন্তু গুরুতর সমস্যাগুলো অযত্নে রয়ে গেছে।",
        "english": "Everyone is trying to solve PC errors, but serious issues have been neglected.",
        "banglish": "PC error somadhane shobai cheshta korche, kintu gurutoro shomossha gulo ojonne roye geche."
    },
    {
        "bangla": "কোডিং এররগুলো নিয়ে আমাদের গ্রুপে অনেক আলোচনা হচ্ছে, কিন্তু সমাধানের পথ খুঁজে পাচ্ছি না।",
        "english": "There’s a lot of discussion in our group about coding errors, but we can’t find a solution.",
        "banglish": "Coding error gulo niye amader group e onek alochona hochche, kintu amra solution khujte pachchi na."
    },
    {
        "bangla": "বাংলাদেশের ভবিষ্যৎ নিয়ে অনেক আলোচনা চলছে, কিন্তু কার্যকর পদক্ষেপ দেখা যাচ্ছে না।",
        "english": "There’s a lot of discussion about the future of Bangladesh, but no effective measures are in sight.",
        "banglish": "Bangladesher bhobishwot niye onek alochona cholche, kintu kargokor podokhep dekha jacche na."
    },
    {
        "bangla": "আন্তর্জাতিক সম্পর্ক নিয়ে অনেক জটিলতা চলছে, কিন্তু সঠিক সমাধান নেই।",
        "english": "There are many complexities in international relations, but no correct solutions.",
        "banglish": "Antorjatik somprok er niye onek jotilota cholche, kintu shothik somadhan nei."
    },
    {
        "bangla": "ইতিহাসের কিছু বিষয় নিয়ে ছাত্ররা বিভক্ত, বিশেষ করে স্বাধীনতা যুদ্ধ।",
        "english": "Students are divided on certain historical topics, especially the Liberation War.",
        "banglish": "Itihas er kichu bishoy niye chhatra ra bibhokto, bishesh kore shadhinota juddho."
    },
    {
        "bangla": "অর্থনীতি নিয়ে একটি গুরুত্বপূর্ণ আলোচনা চলছে, কিন্তু দেশের বর্তমান পরিস্থিতি নিয়ে কিছুই হচ্ছে না।",
        "english": "An important discussion is going on about economics, but nothing is being done about the current situation in the country.",
        "banglish": "Orthonoiti niye ekta gurutopurno alochona cholche, kintu desher bortoman poristithi niye kichui hochche na."
    },
    {
        "bangla": "বাংলাদেশের অর্থনৈতিক পরিস্থিতি নিয়ে উদ্বেগ বাড়ছে, কিন্তু কোনো কার্যকর পদক্ষেপ নেই।",
        "english": "Concerns are rising about the economic situation in Bangladesh, but no effective measures are in place.",
        "banglish": "Bangladesher ortho shomoshyar niye udvigno barche, kintu kono kargokor podokhep nei."
    },
    {
        "bangla": "করোনাভাইরাসের কারণে শিক্ষা ব্যবস্থা পুরোপুরি ভেঙে পড়েছে।",
        "english": "The education system has completely collapsed due to the coronavirus.",
        "banglish": "Koronabirus er karone shikkha byabostha puropurite venge poreche."
    },
    {
        "bangla": "মহামারী নিয়ে অনেক বিতর্ক হচ্ছে, কিন্তু সঠিক তথ্য প্রাপ্তি কঠিন।",
        "english": "There’s a lot of debate about the epidemic, but obtaining accurate information is difficult.",
        "banglish": "Mohamari niye onek bitorko hochhe, kintu shothik totho prapti kothin."
    },
    {
        "bangla": "সামাজিক অবিচার নিয়ে আমাদের মধ্যে আলোচনা চলছে, কিন্তু সঠিক সমাধানের অভাব।",
        "english": "There’s a discussion among us about social injustice, but a lack of effective solutions.",
        "banglish": "Samajik obichar niye amader moddhe alochona cholche, kintu kargokor somadhan er obhab."
    },
    {
        "bangla": "ইউটিউবে একটি নতুন ভিডিও আপলোড হয়েছে, কিন্তু বিষয়বস্তু নিয়ে বিতর্ক রয়েছে।",
        "english": "A new video has been uploaded on YouTube, but there’s controversy over the content.",
        "banglish": "YouTube e ekta notun video upload hoyeche, kintu bishoyboston niye bitorko royeche."
    },
    {
        "bangla": "ফেসবুকে অনেক তথ্য শেয়ার হচ্ছে, কিন্তু সেগুলো সব সত্য নয়।",
        "english": "A lot of information is being shared on Facebook, but not all of it is true.",
        "banglish": "Facebook e onek totho share hochhe, kintu shob totho shotti noy."
    },
    {
        "bangla": "স্ন্যাপচ্যাটে আজকের ঘটনার ছবি শেয়ার করেছে, কিন্তু সঠিক সময় ও স্থান জানা যায়নি।",
        "english": "Photos of today's incident have been shared on Snapchat, but the exact time and place are unknown.",
        "banglish": "Snapchat e ajker ghotonar chhobi share koreche, kintu shothik shomoy o sthan jana jaini."
    },
    {
        "bangla": "ফিজিক্সের পরীক্ষার জন্য আমাদের বেশ কিছু সমস্যা সমাধান করতে হবে, কিন্তু রক্তদানের সময় নেই।",
        "english": "We need to solve several problems for the physics exam, but there's no time for blood donation.",
        "banglish": "Physics er porikkhar jonne amader besh kichu shomossha somadhane korte hobe, kintu roktodaan er shomoy nei."
    },
    {
        "bangla": "কেমিস্ট্রি ক্লাসে আমাদের নতুন রিএকশন শিখতে হবে, কিন্তু অনেকেই অসুস্থ হয়ে পড়ছে।",
        "english": "We need to learn new reactions in chemistry class, but many are falling sick.",
        "banglish": "Chemistry class e amader notun reaction shikhte hobe, kintu onekei osustho hoye porche."
    },
    {
        "bangla": "গণিতে নতুন টপিক নিয়ে আলোচনা চলছে, কিন্তু ছাত্রদের মধ্যে রক্তের অভাব নিয়ে উদ্বেগ রয়েছে।",
        "english": "There's a discussion about a new topic in math, but students are concerned about the shortage of blood.",
        "banglish": "Gonite notun topic niye alochona cholche, kintu chhatroder moddhe rokter obhab niye udvigno royeche."
    },
    {
        "bangla": "আইটি নিয়ে নতুন প্রকল্প শুরু হয়েছে, কিন্তু কিছু সমস্যা হলো যেগুলো সমাধান করতে হবে।",
        "english": "A new project has started in IT, but there are some issues that need solving.",
        "banglish": "IT niye notun projekte shuru hoyeche, kintu kisu shomossha holo jegulo somadhane korte hobe."
    },
    {
        "bangla": "বিগ টেক কোম্পানির শেয়ারের দাম বাড়ছে, কিন্তু তাদের মধ্যে কিছু ইনজুরি রিপোর্ট হয়েছে।",
        "english": "Share prices of big tech companies are rising, but there have been some injury reports among them.",
        "banglish": "Big tech company er share er dam barche, kintu tader moddhe kisu injury report hoyeche."
    },
    {
        "bangla": "এলএলএম প্রযুক্তির ভবিষ্যৎ নিয়ে অনেক আলোচনা চলছে, কিন্তু সঠিক তথ্যের অভাব রয়েছে।",
        "english": "There’s a lot of discussion about the future of LLM technology, but there's a lack of accurate information.",
        "banglish": "LLM projukti er bhobishwot niye onek alochona cholche, kintu shothik totho er obhab royeche."
    },
    {
        "bangla": "টেক সেলিব্রিটিদের নিয়ে নতুন খবর এসেছে, কিন্তু তাদের স্বাস্থ্য নিয়ে উদ্বেগ রয়েছে।",
        "english": "New news has come out about tech celebrities, but there are concerns about their health.",
        "banglish": "Tech celebrities niye notun khobor esheche, kintu tader shastho niye udvigno royeche."
    },
    {
        "bangla": "পিসির সমস্যাগুলো নিয়ে সবাই আলোচনা করছে, কিন্তু গুরুতর বাগগুলি ঠিক করা হয়নি।",
        "english": "Everyone is discussing the issues with PCs, but the serious bugs have not been fixed.",
        "banglish": "PC er shomossha gulo niye shobai alochona korche, kintu gurutoro bug gulo thik kora hoyni."
    },
    {
        "bangla": "কোডিংয়ের সময় অনেক এরর দেখা দিচ্ছে, কিন্তু আমরা রক্তদানে মনোনিবেশ করতে পারছি না।",
        "english": "Many errors are appearing during coding, but we can't focus on blood donation.",
        "banglish": "Coding er shomoy onek error dekha dichche, kintu amra roktodaan e mononibesh korte parchi na."
    },
    {
        "bangla": "বাংলাদেশের অর্থনীতি নিয়ে আলোচনা চলছে, কিন্তু সঠিক পদক্ষেপ নেওয়া হচ্ছে না।",
        "english": "There’s a discussion about the economy of Bangladesh, but no effective steps are being taken.",
        "banglish": "Bangladesher orthoniti niye alochona cholche, kintu kargokor podokhep neya hochche na."
    },
    {
        "bangla": "আন্তর্জাতিক সম্পর্কের ওপর অনেক চাপ বাড়ছে, কিন্তু কারোরই সমস্যা সমাধানের ইচ্ছা নেই।",
        "english": "Pressure is increasing on international relations, but no one wants to solve the problems.",
        "banglish": "Antorjatik somprok er opor onek chap barche, kintu karoroi shomossha somadhaner ichha nei."
    },
    {
        "bangla": "ইতিহাসের কিছু বিষয় নিয়ে বিতর্ক চলছে, কিন্তু রক্তদানের ঘটনা ঘটছে।",
        "english": "There’s a debate about certain historical topics, but incidents of blood donation are occurring.",
        "banglish": "Itihas er kichu bishoy niye bitorko cholche, kintu roktodaan er ghotona ghotche."
    },
    {
        "bangla": "অর্থনীতি নিয়ে আমাদের মধ্যে আলোচনা চলছে, কিন্তু দেশের পরিস্থিতি নিয়ে চিন্তাভাবনা করতে হবে।",
        "english": "We are discussing economics, but we need to think about the country's situation.",
        "banglish": "Amra orthoniti niye alochona korchi, kintu desher poristhiti niye chinta bhabona korte hobe."
    },
    {
        "bangla": "করোনার কারণে স্বাস্থ্যসেবা নিয়ে আলোচনা চলছে, কিন্তু সমস্যা সমাধানে কেউ এগিয়ে আসছে না।",
        "english": "There’s a discussion about healthcare due to the coronavirus, but no one is stepping up to solve the problems.",
        "banglish": "Koronar karone shastho sheba niye alochona cholche, kintu keu shomossha somadhane egiye asche na."
    },
    {
        "bangla": "মহামারীর সময় সামাজিক সমস্যা নিয়ে চিন্তা করতে হবে, কিন্তু সঠিক সমাধানের অভাব।",
        "english": "We need to think about social issues during the epidemic, but there is a lack of effective solutions.",
        "banglish": "Mohamari er shomoy samajik shomossha niye chinta korte hobe, kintu kargokor somadhan er obhab."
    },
    {
        "bangla": "ইউটিউবে ভিডিও আপলোড হচ্ছে, কিন্তু বিষয়বস্তু নিয়ে বিতর্ক তৈরি হয়েছে।",
        "english": "Videos are being uploaded on YouTube, but controversy has arisen over the content.",
        "banglish": "YouTube e video upload hochhe, kintu bishoyboston niye bitorko toiri hoyeche."
    },
    {
        "bangla": "ফেসবুকে অনেক তথ্য শেয়ার হচ্ছে, কিন্তু সেগুলো বিশ্বাসযোগ্য নয়।",
        "english": "Many pieces of information are being shared on Facebook, but they are not trustworthy.",
        "banglish": "Facebook e onek totho share hochhe, kintu segulo bishwasjogyo noy."
    },
    {
        "bangla": "স্ন্যাপচ্যাটে আজকের বিষয় নিয়ে সবাই কথা বলছে, কিন্তু সঠিক তথ্য নেই।",
        "english": "Everyone is talking about today's topic on Snapchat, but there is no accurate information.",
        "banglish": "Snapchat e ajker bishoy niye shobai kotha bolche, kintu ekhane shothik totho nei."
    }
]

def load_data(label_df,df):
     
     for i in range(len(df)):

        label_df.loc[len(label_df)] = [df.loc[i]['English'],0]
        label_df.loc[len(label_df)] = [df.loc[i]['Banglish'],0]
        label_df.loc[len(label_df)] = [df.loc[i]['Bangla'],0]

     return label_df

# df1 = pd.read_csv('./negative-samples/random_messages.csv')
# df2 = pd.read_csv('./negative-samples/random_messages_new.csv')

# label_df = pd.DataFrame(columns=['message','label'])

# label_df = load_data(label_df,df1)
# label_df = load_data(label_df,df2)

label_df = pd.read_csv('./negative-samples/negative.csv')

print(len(label_df))

# label_df.to_csv('negative.csv',index=False)

# preparing positive samples

START_DIRECTORY = './positive-samples/'

start = 0
end = 701 

for i in range(start,end+1):
    
    file_name = f"{START_DIRECTORY}{i}.json"

    if os.path.exists(file_name):
        
        # print(f"{file_name} found")

        with open(file_name,"r",encoding='utf-8') as file:
            
            data = json.load(file)

            label_df.loc[len(label_df)] = [data['message'],1]



# print(f'positive : {(label_df['label']==1).sum()}')

# print(f' {anik_samples[0]['english']}')

print(f'anik samples length: {len(anik_samples)*3}')
for sample in anik_samples:

    categories = ['bangla']

    for cat in categories:

        label_df.loc[len(label_df)] = [sample[cat],0]

print(len(label_df))
print(f'negative: {(label_df['label']==0).sum()}')

label_df.to_csv('bengali-dataset.csv',index=False)

