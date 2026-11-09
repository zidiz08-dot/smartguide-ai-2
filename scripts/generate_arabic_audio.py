"""Generate pre-recorded Arabic alerts for SmartGuide's browser fallback.
Requires: pip install edge-tts
Audio is generated during GitHub Actions and served as static MP3s.
"""
import asyncio
from pathlib import Path
import edge_tts

OUT=Path("audio/ar");OUT.mkdir(parents=True,exist_ok=True)
PHRASES={
"test":"مرحباً، أنا سمارت جايد. الصوت العربي يعمل الآن.",
"warning":"تنبيه. هذا نظام تجريبي ولا يمكن الاعتماد عليه للمشي المستقل.",
"unknown":"لا يمكن التأكد من خلو الطريق من العوائق.",
"person":"شخص","chair":"كرسي","dining table":"طاولة","cup":"كوب","bottle":"زجاجة","book":"كتاب","cell phone":"هاتف","laptop":"حاسوب محمول","tv":"شاشة","backpack":"حقيبة","handbag":"حقيبة يد","suitcase":"حقيبة سفر","bench":"مقعد","couch":"أريكة","bed":"سرير","car":"سيارة","bus":"حافلة","truck":"شاحنة","bicycle":"دراجة","motorcycle":"دراجة نارية","dog":"كلب","cat":"قطة","traffic light":"إشارة مرور","stop sign":"علامة توقف","potted plant":"نبتة","clock":"ساعة","keyboard":"لوحة مفاتيح","mouse":"فأرة حاسوب","refrigerator":"ثلاجة","microwave":"ميكروويف","oven":"فرن","sink":"مغسلة","toilet":"مرحاض","umbrella":"مظلة","sports ball":"كرة","banana":"موز","apple":"تفاحة","orange":"برتقالة","sandwich":"شطيرة","scissors":"مقص","knife":"سكين","fork":"شوكة","spoon":"ملعقة",
"left":"على يسار الصورة","center":"في وسط الصورة","right":"على يمين الصورة",
"detected":"تم اكتشاف","observed":"رُصد","and":"و"
}
async def one(name,text,sem):
    async with sem:
        for attempt in range(3):
            try:
                await edge_tts.Communicate(text,voice="ar-AE-FatimaNeural",rate="-5%").save(str(OUT/(name+".mp3")))
                return
            except Exception:
                if attempt==2:raise
                await asyncio.sleep(2*(attempt+1))
async def main():
    sem=asyncio.Semaphore(3)
    await asyncio.gather(*(one(k,v,sem) for k,v in PHRASES.items()))
    print("Generated",len(PHRASES),"Arabic voice files")
if __name__=="__main__":asyncio.run(main())
