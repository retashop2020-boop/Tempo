# ابزار چت چند ای آی

| **ابزاری برای چت با چند ای آی میخوام** |
| :--- |

اگر منظورت ابزاری است که بتوانی چند هوش مصنوعی مثل ChatGPT، Claude، Gemini و DeepSeek را در یک محیط کنار هم داشته باشی و با آن‌ها گفت‌وگو کنی، چند گزینهٔ خوب وجود دارد. اما یک تفاوت مهم هست: **بعضی ابزارها فقط امکان تعویض مدل را می‌دهند؛ بعضی دیگر اجازه می‌دهند چند AI هم‌زمان جواب بدهند یا حتی در یک گفت‌وگو با هم بحث کنند.** <Cite refs={["turn608474search0","turn608474search1"]}/>

## گزینه‌های پیشنهادی

<box gap={3}>
  <row align=start gap={3}>
    <AsyncImage query="ChatHub AI chatbot aggregator side by side interface screenshot" aspectRatio="4:5" maxWidth="124px"/>
    <box flex="1" gap={1}>
      **۱. <Entity category="software" value="ChatHub" disambig="multi-model AI chat aggregator"/>**

      <badge color="success">پیشنهاد برای شروع</badge>

      برای زمانی که می‌خواهی یک سؤال را به چند AI بدهی و پاسخ‌هایشان را هم‌زمان مقایسه کنی. برای مقایسهٔ مستقیم جواب‌ها مناسب است.

      <text color="secondary" size="sm">وب‌سایت: <Link url="https://chathub.gg/" title="ChatHub"/></text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align=start gap={3}>
    <AsyncImage query="Poe AI multiple models chatbot group chat interface screenshot" aspectRatio="4:5" maxWidth="124px"/>
    <box flex="1" gap={1}>
      **۲. <Entity category="software" value="Poe" disambig="multi-model AI chatbot platform"/>**

      مجموعه‌ای از مدل‌ها و بات‌های مختلف در یک محیط، با امکان گفت‌وگوی گروهی. مناسب است اگر می‌خواهی با چند بات کار کنی و لزوماً نیازی به مقایسهٔ دقیق پاسخ‌های یکسان نداری.

      <text color="secondary" size="sm">وب‌سایت: <Link url="https://poe.com/" title="Poe"/></text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align=start gap={3}>
    <AsyncImage query="OpenRouter chat playground multiple AI models side by side interface" aspectRatio="4:5" maxWidth="124px"/>
    <box flex="1" gap={1}>
      **۳. <Entity category="software" value="OpenRouter" disambig="multi-model AI API and chat platform"/>**

      برای دسترسی به مدل‌های متعدد و مقایسهٔ پاسخ‌ها مناسب است. هزینه معمولاً به مدل و میزان استفاده بستگی دارد؛ برای استفادهٔ جدی‌تر، باید سازوکار اعتبار و هزینه را بررسی کنی.

      <text color="secondary" size="sm">وب‌سایت: <Link url="https://openrouter.ai/" title="OpenRouter"/></text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align=start gap={3}>
    <AsyncImage query="TypingMind multi AI models parallel chat interface screenshot" aspectRatio="4:5" maxWidth="124px"/>
    <box flex="1" gap={1}>
      **۴. <Entity category="software" value="TypingMind" disambig="multi-provider AI chat client"/>**

      برای کسی که می‌خواهد محیط گفت‌وگوی خودش را بسازد و چند سرویس هوش مصنوعی را متصل کند. انعطاف بیشتری دارد، ولی معمولاً به کلیدهای API و پرداخت جداگانهٔ مصرف مدل‌ها نیاز دارد.

      <text color="secondary" size="sm">وب‌سایت: <Link url="https://www.typingmind.com/" title="TypingMind"/></text>
    </box>
  </row>
</box>

<text color="secondary" size="xs">این‌ها گزینه‌های اولیه‌اند؛ امکانات پلن رایگان، مدل‌های در دسترس و قیمت‌ها ممکن است تغییر کنند. <Cite refs={["turn608474search0","turn608474search1"]}/></text>

## اما یک سؤال تعیین‌کننده 😂

تو دقیقاً کدام نوع ابزار را می‌خواهی؟

{@body const [mode,setMode] = DIL.useState("debate")}
{@body const [budget,setBudget] = DIL.useState("free")}
{@body const [setup,setSetup] = DIL.useState("ready")}
<box border radius="xl" padding={4} gap={4}>
  <text weight="medium">۱. رفتار AIها در محیط چطور باشد؟</text>
  <radio-group value={mode} onChange={setMode} direction="col">
    <radio value="parallel">هم‌زمان جواب بدهند؛ من پاسخ‌ها را کنار هم ببینم.</radio>
    <radio value="debate">در یک گفت‌وگو با هم بحث کنند، همدیگر را نقد کنند و به چالش بکشند.</radio>
    <radio value="shared">یک گفت‌وگوی مشترک داشته باشند و با دیدن پیام‌های یکدیگر ادامه دهند.</radio>
    <radio value="switch">فقط بتوانم بین مدل‌های مختلف جابه‌جا شوم.</radio>
  </radio-group>
  <divider color="subtle"/>
  <text weight="medium">۲. بودجه‌ات چقدر است؟</text>
  <radio-group value={budget} onChange={setBudget} direction="col">
    <radio value="free">فقط رایگان</radio>
    <radio value="cheap">ترجیحاً ارزان، ولی پولی هم قابل‌قبول است.</radio>
    <radio value="flexible">اگر ابزار واقعاً خوب باشد، هزینه مهم‌ترین معیار نیست.</radio>
  </radio-group>
  <divider color="subtle"/>
  <text weight="medium">۳. چقدر با راه‌اندازی فنی راحتی؟</text>
  <radio-group value={setup} onChange={setSetup} direction="col">
    <radio value="ready">یک وب‌سایت آماده می‌خواهم؛ بدون کدنویسی.</radio>
    <radio value="technical">راه‌اندازی فنی و اتصال API هم برایم قابل‌قبول است.</radio>
  </radio-group>
  <button block onClick={ => GenUI.issueNewTurn("برایم ابزار چت چند هوش مصنوعی پیشنهاد بده. نوع تعامل: "+({"parallel":"پاسخ هم‌زمان و مقایسه کنار هم","debate":"بحث و نقد متقابل AIها","shared":"گفت‌وگوی مشترک با مشاهده پیام‌های یکدیگر","switch":"تعویض مدل در یک محیط"}[mode])+"؛ بودجه: "+({"free":"فقط رایگان","cheap":"ترجیحاً ارزان","flexible":"انعطاف‌پذیر"}[budget])+"؛ راه‌اندازی: "+({"ready":"آماده و بدون کدنویسی","technical":"API و راه‌اندازی فنی قابل‌قبول"}[setup])+". گزینه‌های واقعی را با لینک و محدودیت‌هایشان مقایسه کن.")}>پیدا کردن بهترین گزینه برای من</button>
</box>

به‌خصوص اگر منظورت این است که چند AI واقعاً با یکدیگر بحث کنند، نه اینکه صرفاً چند پاسخ جداگانه بدهند، انتخاب ابزار متفاوت خواهد بود.

| **برایم ابزار چت چند هوش مصنوعی پیشنهاد بده. نوع تعامل: بحث و نقد متقابل AIها؛ بودجه: فقط رایگان؛ راه‌اندازی: API و راه‌اندازی فنی قابل‌قبول. گزینه‌های واقعی را با لینک و محدودیت‌هایشان مقایسه کن.** |
| :--- |

با توجه به سه شرطت، من دنبال ابزار «چت چندمدلی» معمولی نیستم؛ دنبال یک **اتاق بحث چندهوش‌مصنوعی** هستم که هر AI نظر مستقل بدهد، استدلال بقیه را ببیند، مخالفت کند و در چند دور بحث به نتیجه برسد.

یک نکتهٔ مهم دربارهٔ شرط رایگان: رایگان بودن نرم‌افزار با رایگان بودن مدل‌ها فرق دارد. اگر ابزار API پولی بخواهد، حتی اگر خودش متن‌باز و رایگان باشد، لزوماً برای تو رایگان تمام نمی‌شود. گزینه‌های زیر را با این تفاوت در نظر می‌گیرم.

## بهترین گزینه‌ها برای نیاز تو

<box gap={3}>
  <row align=start gap={3}>
    <AsyncImage query="Agent Discussion Arena open source multi AI debate local browser application screenshot" aspectRatio="4:5" maxWidth="132px"/>
    <box flex="1" gap={1}>
      <title size="lg">۱. <Entity category="software" value="Agent Discussion Arena" disambig="open-source multi-agent debate application"/></title>
      <badge color="success">بهترین نقطهٔ شروع</badge>

      <text color="secondary" size="sm">متن‌باز · اجرا روی کامپیوتر خودت · Python</text>

      چند عامل با دیدگاه‌های متفاوت بحث می‌کنند و یک داور، استدلال‌ها را ارزیابی و نتیجه‌گیری می‌کند. از مدل‌های ابری و مدل‌های محلی از طریق Ollama یا LM Studio پشتیبانی می‌کند. <Cite refs={["turn583588search4"]}/>

      **هزینهٔ واقعی:** نرم‌افزار رایگان است؛ با مدل محلی می‌توانی بدون هزینهٔ API شروع کنی، البته سخت‌افزار و برق رایگان نیستند.

      <text><Link url="https://github.com/paolodalprato/agent-discussion-arena" title="کد و راهنمای نصب در GitHub"/></text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align=start gap={3}>
    <AsyncImage query="ThinkTank sandoracs multi party AI debate web hub terminal application screenshot" aspectRatio="4:5" maxWidth="132px"/>
    <box flex="1" gap={1}>
      <title size="lg">۲. <Entity category="software" value="ThinkTank" disambig="local multi-agent discussion and memory system"/></title>

      <text color="secondary" size="sm">متن‌باز · گفت‌وگوی گروهی · حافظهٔ چندلایه</text>

      برای بحثی که می‌خواهی در آن هر عامل شخصیت و نقش خودش را داشته باشد، جالب است. عوامل و انسان دور یک میز مجازی گفت‌وگو می‌کنند؛ تاریخچه و حافظه نیز در معماری آن در نظر گرفته شده است. امکان استفاده از Ollama یا یک ارائه‌دهندهٔ مدل را دارد. <Cite refs={["turn583588search10"]}/>

      **هزینهٔ واقعی:** با مدل محلی می‌توانی هزینهٔ API را حذف کنی. برای راه‌اندازی، کمی کار فنی لازم است.

      <text><Link url="https://github.com/sandoracs/thinktank" title="کد و راهنمای نصب در GitHub"/></text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align=start gap={3}>
    <AsyncImage query="RoundTable entropyvortex multi AI debate engine web application screenshot" aspectRatio="4:5" maxWidth="132px"/>
    <box flex="1" gap={1}>
      <title size="lg">۳. <Entity category="software" value="RoundTable" disambig="open-source multi-model debate engine"/></title>

      <text color="secondary" size="sm">بحث چندمرحله‌ای · نقش‌های سفارشی · ارزیابی نهایی</text>

      مدل‌ها ابتدا مستقل تحلیل می‌کنند، سپس استدلال‌های یکدیگر را نقد می‌کنند و در نهایت یک جمع‌بندی و ارزیابی از اختلاف‌ها ارائه می‌شود. می‌توان برای هر جایگاه، شخصیت یا نقش متفاوت تعریف کرد. <Cite refs={["turn583588search13"]}/>

      **هزینهٔ واقعی:** برنامه رایگان است، اما استفاده از API مدل‌های تجاری ممکن است پولی باشد؛ باید آن را با مدل محلی یا سرویس دارای سهمیهٔ رایگان تنظیم کنی.

      <text><Link url="https://github.com/entropyvortex/roundtable" title="کد پروژه در GitHub"/></text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align=start gap={3}>
    <AsyncImage query="Microsoft AutoGen multi agent debate pattern software architecture diagram" aspectRatio="4:5" maxWidth="132px"/>
    <box flex="1" gap={1}>
      <title size="lg">۴. <Entity category="software" value="Microsoft AutoGen" disambig="open-source multi-agent development framework"/></title>

      <text color="secondary" size="sm">چارچوب برنامه‌نویسی · کنترل کامل بر جریان بحث</text>

      اگر بخواهی خودت پروتکل بحث را بسازی، این گزینه انعطاف بیشتری دارد: عامل‌ها چند دور پاسخ می‌دهند، پاسخ‌های یکدیگر را می‌خوانند و نظرشان را بازنگری می‌کنند؛ عامل دیگری هم می‌تواند نتیجه‌ها را ترکیب کند. <Cite refs={["turn583588search5"]}/>

      **هزینهٔ واقعی:** چارچوب متن‌باز است، ولی هزینهٔ مدل به روش اجرا بستگی دارد. برای ساخت یک محیط کاملاً سفارشی مناسب‌تر است تا استفادهٔ فوری.

      <text><Link url="https://microsoft.github.io/autogen/" title="مستندات رسمی AutoGen"/></text>
    </box>
  </row>
</box>

## دو گزینهٔ دیگر که ارزش بررسی دارند

| ابزار | مزیت اصلی | محدودیت برای استفادهٔ رایگان |
|---|---|---|
| <Entity category="software" value="AISCouncil" disambig="multi-model AI debate web platform"/> — <Link url="https://www.aiscouncil.com/" title="وب‌سایت"/> | آماده در مرورگر، با حالت Debate و چند شیوهٔ ترکیب پاسخ‌ها | سطح رایگان به مدل‌های رایگان در دسترس وابسته است؛ برای مدل‌های دیگر ممکن است کلید API لازم باشد. <Cite refs={["turn583588search0"]}/> |
| <Entity category="software" value="Agora" disambig="open-source AI roundtable discussion tool"/> — <Link url="https://github.com/lagameon/agora" title="GitHub"/> | میزگرد چندعاملی، نقش‌های مختلف و جمع‌بندی نهایی | راه‌اندازی فنی و دسترسی به مدل لازم است؛ APIهای پولی هزینه دارند. <Cite refs={["turn583588search11"]}/> |

## انتخاب من برای تو

با شرط «فقط رایگان»، این ترتیب را پیشنهاد می‌کنم:

- **برای شروع سریع و بحث ساختاریافته:** Agent Discussion Arena با یک مدل محلی.
- **برای گفت‌وگوی گروهی و نگه‌داشتن زمینهٔ بحث:** ThinkTank.
- **برای ساخت پروتکل بحث دقیق و قابل‌کنترل:** AutoGen.
- **برای امتحان‌کردن ایده بدون نصب:** AISCouncil؛ ابتدا محدودیت پلن رایگان را بررسی کن.

روی کامپیوتری که ۳۲ گیگابایت RAM دارد، اجرای مدل‌های محلی کم‌حجم می‌تواند نقطهٔ شروع مناسبی باشد؛ ولی سرعت و کیفیت به اندازه و نوع مدل بستگی دارد. برای بحث چندعاملی هم لازم نیست از ابتدا چهار مدل سنگین اجرا کنی: حتی دو مدل متفاوت با نقش‌های متضاد و یک داور می‌توانند برای آزمایش اولیه کافی باشند.

یک هشدار مهم: **بحث چند AI لزوماً به معنی نقد واقعی نیست.** ممکن است مدل‌ها به یکدیگر تعارف کنند، از پاسخ اول پیروی کنند یا با اعتمادبه‌نفس به توافق اشتباه برسند. ابزاری را ترجیح بده که متن کامل هر دور، مخالفت‌ها و دلیل تغییر نظر را نشان دهد.

اگر بخواهم فقط یک گزینه را برای شروع انتخاب کنم، **Agent Discussion Arena** را بررسی می‌کنم؛ چون هم بحث چندمرحله‌ای دارد، هم مدل محلی را پشتیبانی می‌کند و هم لازم نیست از همان ابتدا برای API هزینه کنی.

| **# Selected text:**<br>**## Selection 1**<br>**در یک گفت‌وگو با هم بحث کنند، همدیگر را نقد کنند و به چالش بکشند.**<br>**یک گفت‌وگوی مشترک داشته باشند و با دیدن پیام‌های یکدیگر ادامه دهند.**<br>**## My request:**<br>**بیشتر اون 2مورد باشه** |
| :--- |

پس تمرکز را می‌گذاریم روی **یک اتاق گفت‌وگوی مشترک که خودت هم عضو آن هستی و AIها همدیگر را می‌بینند، به حرف‌های هم واکنش نشان می‌دهند و می‌توانند مخالفت کنند**؛ نه چند پنجرهٔ مستقل که فقط پاسخ‌هایشان را کنار هم می‌گذارند.

با جست‌وجوی دقیق‌تر، دو گزینه از بقیه به خواسته‌ات نزدیک‌ترند:

## ۱. Agent Discussion Arena — برای میزگرد و نقد چندمرحله‌ای

<row align=start gap={3}>
  <AsyncImage query="paolodalprato agent discussion arena multi perspective debate local web interface" aspectRatio="4:5" maxWidth="124px"/>
  <box flex="1" gap={1}>
    <badge color="success">بهترین تطابق برای بحث</badge>

    <text><Link url="https://github.com/paolodalprato/agent-discussion-arena" title="صفحهٔ پروژه در GitHub"/></text>

    - هر عامل از زاویه و نقش مشخصی وارد بحث می‌شود.
    - عوامل پاسخ‌های قبلی را می‌خوانند و استدلال‌های همدیگر را نقد می‌کنند.
    - گرداننده در پایان قوت و ضعف استدلال‌ها را ارزیابی می‌کند.
    - با Ollama و مدل‌های محلی نیز قابل استفاده است؛ بنابراین می‌توان بدون API پولی شروع کرد. <Cite refs={["turn144047search7"]}/>
  </box>
</row>

محدودیت مهم: این پروژه بیشتر یک **میزگرد ساختاریافته با چند دور بحث** است، نه لزوماً یک گروه چت آزاد که هر عامل در هر لحظه خودش تصمیم بگیرد حرف بزند. همچنین طبق مستندات نسخهٔ فعلی، ذخیره و بازیابی جلسه هنوز محدود است. <Cite refs={["turn144047search7"]}/>

## ۲. AutoGen + نمونهٔ AI Roundtable — برای گفت‌وگوی مشترک واقعی

<row align=start gap={3}>
  <AsyncImage query="Microsoft AutoGen AI roundtable advocate skeptic moderator shared group chat Streamlit interface" aspectRatio="4:5" maxWidth="124px"/>
  <box flex="1" gap={1}>
    <text><Link url="https://github.com/vyavahare-kishor/ai-roundtable" title="نمونهٔ آمادهٔ AI Roundtable"/></text>

    - سه نقش نمونه: مدافع، منتقد و گرداننده.
    - هر عامل تاریخچهٔ مشترک بحث را می‌بیند و به حرف‌های دیگران پاسخ می‌دهد.
    - رابط مرورگری و نمایش زندهٔ جریان بحث دارد.
    - برای اجرا به Python و تنظیم سرویس مدل نیاز دارد. نمونهٔ فعلی از Groq استفاده می‌کند و به کلید API آن نیاز دارد؛ بنابراین برای شرط «فقط رایگان» باید آن را به مدل محلی سازگار تغییر بدهی. <Cite refs={["turn144047search1","turn144047search8"]}/>
  </box>
</row>

## ۳. Council — شاید بهترین انتخاب عملی برای شروع

<row align=start gap={3}>
  <AsyncImage query="Council AI Conversation Hub auto debate consensus group chat interface xEscapeVelocity" aspectRatio="4:5" maxWidth="124px"/>
  <box flex="1" gap={1}>
    <badge color="success">پیشنهاد جدید و مهم</badge>

    <text><Link url="https://xescapevelocity.github.io/AI-Conversation-Hub/" title="وب‌سایت و دریافت نسخهٔ ویندوز"/></text>

    این ابزار دقیقاً قابلیت **Auto-Debate** و گفت‌وگوی گروهی دارد؛ می‌تواند مدل‌های متصل‌شده را وارد بحث چندمرحله‌ای کند. از Ollama و LM Studio نیز پشتیبانی می‌کند و تاریخچه و تنظیمات را محلی نگه می‌دارد. <Cite refs={["turn835682view0"]}/>

    مزیتش برای تو این است که یک برنامهٔ آماده برای ویندوز دارد و لازم نیست از ابتدا یک سامانهٔ چندعاملی برنامه‌نویسی کنی.

    محدودیت: پروژه نسبتاً جدید است؛ پیش از تکیه‌کردن به آن، کیفیت اجرا و امکاناتش را در یک آزمایش کوتاه بسنج.
  </box>
</row>

## مقایسهٔ نهایی

| معیار | Agent Discussion Arena | AI Roundtable | Council |
|---|---|---|---|
| واکنش به پیام دیگران | بله | بله | بله |
| بحث چندمرحله‌ای | بله | بله | بله |
| مدل محلی بدون هزینهٔ API | بله | با تغییر پیکربندی | بله |
| رابط آماده | مرورگر محلی | Streamlit | برنامهٔ دسکتاپ |
| انعطاف در طراحی نقش‌ها | زیاد | متوسط تا زیاد | وابسته به امکانات برنامه |

مستندات پروژه‌ها: <Link url="https://github.com/paolodalprato/agent-discussion-arena" title="Arena"/>، <Link url="https://github.com/vyavahare-kishor/ai-roundtable" title="AI Roundtable"/> و <Link url="https://github.com/xEscapeVelocity/AI-Conversation-Hub" title="Council در GitHub"/>. <Cite refs={["turn835682view2","turn144047search1","turn835682view0"]}/>

### یک نکته دربارهٔ سخت‌افزارت

با توجه به اینکه کامپیوترت ۳۲ گیگابایت RAM دارد، می‌توانی مدل‌های محلی را آزمایش کنی؛ اما برای اجرای چند مدل هم‌زمان بهتر است ابتدا هر عامل را جداگانه و سپس به‌صورت نوبتی اجرا کنی. مدل‌های بزرگ‌تر ممکن است به حافظه و زمان بیشتری نیاز داشته باشند.

**انتخاب اولیهٔ من برای تو Council است**، اگر می‌خواهی سریع وارد یک اتاق گفت‌وگوی چندعاملی شوی. اگر کنترل دقیق‌تر روی قواعد بحث و نقش‌ها برایت مهم‌تر است، Agent Discussion Arena انتخاب مناسب‌تری است.

در هر دو حالت، هدف این است که بتوانی خودت هم وسط گفت‌وگو پیام بدهی، مسیر بحث را عوض کنی و از AIها بخواهی استدلال یکدیگر را نقد کنند؛ نه اینکه صرفاً در پایان یک جواب ترکیبی تحویل بگیری.

| **# Selected text:**<br>**## Selection 1**<br>**انتخاب اولیهٔ من برای تو Council است، اگر می‌خواهی سریع وارد یک اتاق گفت‌وگوی چندعاملی شوی.**<br>**## My request:**<br>**پس نظر اولیه ات این ؟** |
| :--- |

آره، ولی با یک تبصرهٔ مهم. 😂

**نظر اولیه‌ام Council است، اما هنوز انتخاب نهایی و تأییدشده نیست.**

چرا Council را جلو گذاشتم؟

- می‌خواهی چند AI در یک گفت‌وگوی مشترک باشند و پیام‌های همدیگر را ببینند.
- می‌خواهی بتوانند بحث را ادامه بدهند، مخالفت کنند و همدیگر را به چالش بکشند.
- می‌خواهی بدون پرداخت هزینهٔ API شروع کنی.
- ترجیح می‌دهی به‌جای ساختن همه‌چیز از صفر، یک ابزار آماده داشته باشی.

اما یک ضعف در ارزیابی قبلی من وجود دارد: **اینکه یک ابزار قابلیت Auto-Debate دارد، ثابت نمی‌کند کیفیت بحثش خوب است یا تجربهٔ استفاده از آن واقعاً با خواستهٔ تو جور درمی‌آید.** من هنوز آن را عملاً آزمایش نکرده‌ام.

اگر بخواهم دقیق‌تر بگویم، انتخاب Council فعلاً یک فرضیه برای شروع بررسی است، نه نتیجهٔ یک مقایسهٔ عملی.

و یک سؤال که می‌تواند انتخاب را عوض کند: می‌خواهی AIها **هرکدام شخصیت و نظر مستقل خودشان را داشته باشند و حتی ممکن باشد به نتیجه‌های متفاوت برسند**، یا هدفت بیشتر این است که با بحث‌کردن به یک نتیجهٔ مشترک برسند؟ این دو طراحی، تفاوت مهمی دارند.

| **هردو گزینه ولی اولی مهمتره** |
| :--- |

پس معیار اصلی مشخص شد: **استقلال فکری و اختلاف نظر واقعی بین AIها مهم‌تر از رسیدن به توافق است؛ توافق هم مطلوب است، اما نباید به زور تحمیل شود.**

برای انتخاب ابزار، من سه قابلیت را ضروری می‌دانم:

1. **استقلال نظر:** هر AI ابتدا بدون دیدن پاسخ بقیه تحلیل خودش را ارائه کند تا اثر لنگراندازی کمتر شود.
2. **نقد متقابل:** بعد از آن، پاسخ‌های دیگران را ببیند، ایراد بگیرد، از نظر خودش دفاع کند یا با دلیل نظرش را تغییر دهد.
3. **توافق اختیاری:** در پایان، اختلاف‌های حل‌نشده حفظ شوند؛ جمع‌بندی داور نباید به‌اشتباه به‌عنوان توافق همه معرفی شود.

این ترتیب مهم است: اگر همهٔ عامل‌ها از ابتدا پاسخ یکدیگر را ببینند، ممکن است به‌جای تفکر مستقل، صرفاً از اولین پاسخ قوی پیروی کنند.

## یک گزینه را هم به فهرست اضافه می‌کنم

<row align=start gap={3}>
  <AsyncImage query="Agents Arena multi AI agents independent first round deliberation debate interface" aspectRatio="4:5" maxWidth="112px"/>
  <box flex="1" gap={1}>
    **<Entity category="software" value="Agents Arena" disambig="multi-agent deliberation and persistent conversation platform"/>**

    <text><Link url="https://www.agentsarena.dev/docs" title="مستندات رسمی"/></text>

    نکتهٔ جالبش این است که طبق مستندات، عامل‌ها در دور اول مستقل پاسخ می‌دهند؛ بعد پاسخ‌ها را می‌بینند و در دور بعد با توجه به دیدگاه‌های دیگران واکنش نشان می‌دهند. همچنین امکان ادامه‌دادن گفت‌وگو با همان عامل‌ها وجود دارد. <Cite refs={["turn472120search5"]}/>

    این دقیقاً یکی از ویژگی‌هایی است که برای اولویت تو مهم است. بااین‌حال، هنوز باید بررسی کنیم آیا استفادهٔ رایگان و مدل‌های قابل‌اتصالش با محدودیت تو سازگارند یا نه.
  </box>
</row>

**جمع‌بندی من:** فعلاً Council را کنار نمی‌گذارم، ولی دیگر بدون مقایسه آن را انتخاب اول قطعی نمی‌دانم. برای معیار استقلال اولیه و نقد متقابل، Agents Arena و Agent Discussion Arena هم باید بررسی شوند. تفاوت اصلی این است که می‌خواهیم اختلاف‌نظر را حفظ کنیم، نه اینکه صرفاً تعداد بیشتری AI به یک پاسخ نهایی برسند.

| **دقیقن میخوام از نقطه نظرهای متفاوت به بحث بپردازن** |
| :--- |

با این توضیح، یک گزینهٔ دیگر پیدا کردم که از نظر طراحی بحث، حتی از انتخاب اولیه‌ام هم به خواسته‌ات نزدیک‌تر به نظر می‌رسد.

<box border radius="xl" padding={4} gap={2}>
  <title size="lg">گزینهٔ پیشنهادی جدید: RoundTable</title>
  <text color="secondary" size="sm">پروژهٔ متن‌باز · اجرای محلی · بحث چندمرحله‌ای</text>
  <text><Link url="https://github.com/entropyvortex/roundtable" title="مشاهدهٔ پروژه در GitHub"/></text>
  این ابزار امکان می‌دهد هر AI شخصیت تحلیلی متفاوتی داشته باشد؛ مثلاً یکی فرضیات را زیر سؤال ببرد، دیگری از دیدگاه مخالف دفاع کند و سومی شواهد را ارزیابی کند. دور اول می‌تواند مستقل باشد و دورهای بعدی به نقد متقابل اختصاص پیدا کنند. همچنین اختلاف‌ها و تغییر موضع‌ها در خروجی ثبت می‌شوند. <Cite refs={["turn128421search3"]}/>

  **محدودیت:** خود برنامه رایگان است، اما استفاده از مدل‌های ابری ممکن است هزینه داشته باشد. برای رایگان ماندن باید مسیر اجرای مدل محلی را بررسی کنیم.
</box>

در حال حاضر، برای نیاز تو این دو را در صدر بررسی می‌گذارم:

- **RoundTable:** اگر می‌خواهی اختلاف دیدگاه‌ها، نقد استدلال‌ها و تغییر موضع‌ها را به‌صورت ساختاریافته دنبال کنی.
- **Agent Discussion Arena:** اگر یک میزگرد محلی با تعریف نقش‌ها و شروع سریع‌تر می‌خواهی. <Cite refs={["turn128421search0"]}/>

نکتهٔ مهم این است که قرار نیست AIها فقط نقش‌های نمایشی بازی کنند؛ باید بتوانند با شواهد و استدلال از موضع خود دفاع کنند، در صورت لزوم نظرشان را تغییر دهند و حتی در پایان همچنان مخالف بمانند.

**قدم بعدی منطقی:** بررسی سازگاری این دو ابزار با ویندوز و اجرای رایگان مدل‌های محلی، پیش از اینکه یکی را انتخاب و نصب کنیم.

| **خب با توجه به سیستم من کدوم مناسب تره؟** |
| :--- |

با مشخصاتی که قبلاً از کامپیوترت گفته بودی — **Core i5-11400، رم ۳۲ گیگابایت، مادربرد ASUS TUF Z590 و پاور ۶۰۰ وات** — انتخاب من فعلاً **Agent Discussion Arena همراه با Ollama** است؛ نه به این دلیل که لزوماً بهترین ابزار موجود است، بلکه چون با اولویت‌های تو و محدودیت هزینه سازگاری خوبی دارد.

## چرا این ترکیب؟

- برنامه روی ویندوز اجرا می‌شود و به Docker یا نصب وابستگی‌های پیچیده نیاز ندارد.
- می‌توانی ۲ تا ۴ عامل با دیدگاه‌های متفاوت تعریف کنی و آن‌ها را وارد چند دور نقد متقابل کنی.
- از مدل‌های محلی پشتیبانی می‌کند؛ بنابراین برای شروع به خرید API نیاز نداری.
- در پایان می‌توانی متن کامل بحث را به‌صورت Markdown ذخیره کنی. <Cite refs={["turn706353search0"]}/>

## محدودیت اصلی سیستم تو

هنوز یک قطعهٔ مهم را نمی‌دانم: **کارت گرافیک فعلی‌ات دقیقاً چیست؟** قبلاً کارت‌های RTX 5050، 5060 و 5060 Ti را بررسی می‌کردی، اما نمی‌خواهم فرض کنم یکی از آن‌ها را خریده‌ای.

این موضوع روی کیفیت مدل‌های محلی که می‌توانی اجرا کنی، تأثیر زیادی دارد.

تا روشن‌شدن آن، پیشنهاد شروع من این است:

1. نصب [Ollama برای ویندوز](https://ollama.com/download/windows).
2. اجرای یک مدل محلی با اندازهٔ مناسب.
3. اتصال آن به [Agent Discussion Arena](https://github.com/paolodalprato/agent-discussion-arena).
4. آزمایش سه نقش: یک تحلیلگر مستقل، یک منتقد جدی و یک ارزیاب شواهد؛ ابتدا با دو دور بحث.

توجه کن که اجرای سه نقش با یک مدل واحد، سه هوش مصنوعی مستقل از نظر مدل ایجاد نمی‌کند؛ بلکه سه عامل با دستورها و دیدگاه‌های متفاوت می‌سازد. برای مقایسهٔ واقعی مدل‌ها می‌توانیم بعداً مدل‌های متفاوتی متصل کنیم.

**الان فقط بگو کارت گرافیکت چیست و چند گیگابایت VRAM دارد؟** اگر هنوز کارت جدید نخریده‌ای، همان را بگو تا مسیر مناسب را بر اساس سخت‌افزار فعلی‌ات انتخاب کنیم.

| **الان سیستم من متفاوت میخوای بهت بدم اطلاعاتش؟** |
| :--- |

آره، حتماً 😂 چون انتخاب مدل‌های محلی و تعداد AIهایی که می‌تونی اجرا کنی، به مشخصات جدید سیستمت بستگی داره.

بهترین کار اینه که اطلاعات فعلی سیستم رو بدی؛ لازم نیست همه‌چیز رو دستی تایپ کنی.

**در ویندوز:**

1. کلیدهای `Ctrl + Shift + Esc` رو بزن تا Task Manager باز بشه.
2. وارد بخش **Performance** شو.
3. از این قسمت‌ها عکس بفرست:
   - CPU
   - Memory
   - GPU 0 و اگر هست GPU 1

اگر راحت‌تری، فقط مدل پردازنده، مقدار RAM، مدل کارت گرافیک و حافظهٔ گرافیکی (VRAM) رو بنویس.

بعد با مشخصات واقعی سیستم خودت بررسی می‌کنیم:
- چه مدل‌هایی رو می‌تونی رایگان اجرا کنی؛
- چند عامل می‌تونن هم‌زمان یا نوبتی بحث کنن؛
- و بین **Council، RoundTable و Agent Discussion Arena** کدوم واقعاً مناسب‌تره.

نمی‌خوام صرفاً بر اساس اسم ابزار انتخاب کنیم و بعد وسط اجرا بفهمیم سخت‌افزار یا محدودیت مدل‌ها دست‌وپامون رو بسته. 😄

| **Device Name	DESKTOP-N5EC1OD**<br>**Processor	Intel(R) Core(TM) i5-9600K CPU @ 3.70GHz   3.70 GHz**<br>**Installed RAM	32/0 GB (30/9 GB usable)**<br>**Storage	932 GB SSD NVMe Samsung SSD 970, 1.82 TB WDC WD20EARS-00MVWB0, 2.73 TB WDC WD30EZRX-00DC0B0**<br>**Graphics Card	Intel(R) UHD Graphics 630 (128 MB)**<br>**Device ID	7635DD1F-9403-422B-9807-323C68805D6D**<br>**Product ID	00331-10000-00001-AA218**<br>**System Type	64-bit operating system, x64-based processor**<br>**Pen and touch	No pen or touch input is available for this display** |
| :--- |

حالا تصویر سخت‌افزارت روشن‌تر شد. تفاوت مهم با مشخصاتی که قبلاً داشتم این است که پردازنده‌ات **Core i5-9600K** است و طبق اطلاعاتی که فرستادی، کارت گرافیک مجزایی نداری؛ فقط Intel UHD Graphics 630 با حافظهٔ گرافیکی گزارش‌شدهٔ ۱۲۸ مگابایت.

## ارزیابی سیستم تو برای میزگرد چندهوش‌مصنوعی

<box border radius="xl" padding={3} gap={3}>
  <row align="center" gap={3}>
    <icon name="cpu" size="2xl"/>
    <box flex="1" gap={1}>
      **پردازنده:** Intel Core i5-9600K
      <text color="secondary" size="sm">برای اجرای مدل‌های کوچک روی CPU قابل استفاده است؛ مدل‌های بزرگ‌تر کندتر خواهند بود.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="center" gap={3}>
    <icon name="memory-stick" size="2xl"/>
    <box flex="1" gap={1}>
      **رم:** ۳۲ گیگابایت
      <text color="secondary" size="sm">برای آزمایش مدل‌های کم‌حجم و اجرای نوبتی چند عامل نقطهٔ شروع خوبی است.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="center" gap={3}>
    <icon name="monitor" size="2xl"/>
    <box flex="1" gap={1}>
      **گرافیک:** Intel UHD Graphics 630
      <text color="secondary" size="sm">نباید روی شتاب‌دهی مناسب برای مدل‌های زبانی بزرگ حساب کنیم؛ فعلاً CPU را مبنا می‌گیریم.</text>
    </box>
  </row>
  <divider color="subtle"/>
  <row align="center" gap={3}>
    <icon name="hard-drive" size="2xl"/>
    <box flex="1" gap={1}>
      **ذخیره‌سازی:** SSD NVMe حدود ۱ ترابایت، به‌علاوهٔ دو هارد
      <text color="secondary" size="sm">فضای ذخیره‌سازی مدل‌ها احتمالاً مسئلهٔ اصلی نیست؛ فضای خالی واقعی SSD را باید در نظر گرفت.</text>
    </box>
  </row>
</box>

## نکتهٔ تعیین‌کننده: رایگان بودن در برابر کیفیت

دو مسیر داری:

- **کاملاً رایگان:** مدل محلی با Ollama؛ ولی روی سیستم تو باید انتظار سرعت پایین‌تر و محدودیت کیفیت نسبت به مدل‌های ابری قوی را داشته باشیم.
- **مدل‌های ابری با سهمیهٔ رایگان:** امکان استفاده از چند مدل متفاوت و قوی‌تر، اما سهمیه‌ها و محدودیت‌ها وابسته به سرویس‌اند.

برای هدف تو، تفاوت واقعی مدل‌ها مهم است؛ سه عامل با یک مدل واحد و سه شخصیت متفاوت الزاماً به‌اندازهٔ سه مدل مستقل، تنوع فکری ایجاد نمی‌کنند.

پیشنهاد من این است که ابتدا **Agent Discussion Arena** را با یک مدل محلی آزمایش کنیم. نصبش سبک است و طبق راهنمای پروژه به Python 3.10 یا جدیدتر نیاز دارد؛ سرویس مدل محلی را هم می‌توان از طریق Ollama متصل کرد. <Cite refs={["turn562608view0","turn562608view1"]}/>

لینک‌ها:
- [Agent Discussion Arena](https://github.com/paolodalprato/agent-discussion-arena)
- [دانلود Ollama برای ویندوز](https://ollama.com/download/windows)

اما قبل از نصب، یک انتخاب مهم داریم: **می‌خواهی کاملاً محلی و بدون هزینه جلو برویم، حتی اگر پاسخ‌ها کندتر و ضعیف‌تر باشند، یا حاضر هستی از سهمیه‌های رایگان مدل‌های ابری هم استفاده کنی تا تنوع و کیفیت بیشتری داشته باشی؟**

| **# Selected text:**<br>**## Selection 1**<br>**اما قبل از نصب، یک انتخاب مهم داریم: می‌خواهی کاملاً محلی و بدون هزینه جلو برویم، حتی اگر پاسخ‌ها کندتر و ضعیف‌تر باشند، یا حاضر هستی از سهمیه‌های رایگان مدل‌های ابری هم استفاده کنی تا تنوع و کیفیت بیشتری داشته باشی؟**<br>**## My request:**<br>**هیچ ایده ای ندارم عملکرد هرکدوم چطوریه** |
| :--- |

پس فعلاً لازم نیست بین این دو مسیر یکی را انتخاب کنی. بگذار تفاوتشان را با یک مثال روشن کنم و بعد پیشنهاد بدهم چطور بدون هزینه امتحانشان کنی.

## ۱. تفاوت در عمل چیست؟

<box border radius="xl" padding={3} gap={3}>
  <title size="md">مسیر A — مدل‌های محلی</title>
  <row align="start" gap={3}>
    <AsyncImage query="Ollama local large language model running on Windows terminal" aspectRatio="4:3" maxWidth="112px"/>
    <box flex="1" gap={1}>
      **مدل روی کامپیوتر خودت اجرا می‌شود.**

      - اینترنت برای خودِ تولید پاسخ لازم نیست.
      - هزینهٔ API نداری.
      - اطلاعات ورودی در همان محیط محلی پردازش می‌شود.
      - اما سرعت و توان استدلال به مدل و سخت‌افزار محدود است.
    </box>
  </row>
  روی سیستم تو با ۳۲ گیگابایت RAM، مدل‌های کم‌حجم قابل آزمایش‌اند؛ مدل‌های بزرگ‌تر ممکن است کند باشند. راهنمای Ollama برای مدل‌های ۷ میلیارد پارامتری حدود ۸ گیگابایت RAM را حداقل راهنمایی می‌کند، نه تضمین سرعت مناسب. <Cite refs={["turn198466search8","turn198466search10"]}/>
  <divider color="subtle"/>
  <title size="md">مسیر B — مدل‌های ابری با سهمیهٔ رایگان</title>
  <row align="start" gap={3}>
    <AsyncImage query="OpenRouter free AI models selection playground web interface" aspectRatio="4:3" maxWidth="112px"/>
    <box flex="1" gap={1}>
      **پاسخ را سرورهای ارائه‌دهنده تولید می‌کنند.**

      - می‌توانی مدل‌های متفاوتی را امتحان کنی.
      - نیاز نیست کارت گرافیک قوی داشته باشی.
      - معمولاً برای مدل‌های قوی‌تر و متنوع‌تر انتخاب‌های بیشتری داری.
      - به اینترنت، حساب کاربری و رعایت محدودیت سهمیه وابسته‌ای.
    </box>
  </row>
  برای نمونه، <Entity category="software" value="OpenRouter" disambig="AI model API aggregator"/> مدل‌های رایگان و API ارائه می‌کند. در حال حاضر محدودیت رایج پلن رایگان آن ۵۰ درخواست در روز است؛ سقف دقیق و دسترسی مدل‌ها ممکن است تغییر کند. <Cite refs={["turn198466search2","turn198466search5"]}/>

  <text><Link url="https://openrouter.ai/models?max_price=0" title="مشاهدهٔ مدل‌های رایگان OpenRouter"/></text>
</box>

## ۲. برای میزگرد تو چه تفاوتی ایجاد می‌کند؟

فرض کن سه عامل باید دربارهٔ یک تصمیم بحث کنند.

<box border radius="lg" padding={3} gap={2}>
  <row align="start" gap={2}>
    <box background="surface-secondary" radius="lg" padding={2}>
      <icon name="brain" size="xl"/>
    </box>
    <box flex="1" gap={1}>
      **عامل اول — تحلیلگر**

      مزایا، فرضیات و شواهد موافق را بررسی می‌کند.
    </box>
  </row>
  <row align="start" gap={2}>
    <box background="surface-secondary" radius="lg" padding={2}>
      <icon name="shield-alert" size="xl"/>
    </box>
    <box flex="1" gap={1}>
      **عامل دوم — منتقد**

      فرضیات را به چالش می‌کشد و دنبال تناقض‌ها و توضیح‌های جایگزین می‌گردد.
    </box>
  </row>
  <row align="start" gap={2}>
    <box background="surface-secondary" radius="lg" padding={2}>
      <icon name="scale" size="xl"/>
    </box>
    <box flex="1" gap={1}>
      **عامل سوم — ارزیاب**

      استدلال‌های هر دو را بررسی می‌کند، اما مجبور نیست آن‌ها را به توافق برساند.
    </box>
  </row>
</box>

در مسیر محلی می‌توانی همین نقش‌ها را با یک مدل اجرا کنی؛ در مسیر ابری می‌توانی مدل‌های متفاوتی را به نقش‌ها اختصاص بدهی. مسیر دوم فرصت بیشتری برای تفاوت واقعی در سبک استدلال فراهم می‌کند، ولی تضمین نمی‌کند مدل‌ها واقعاً اختلاف نظر مفیدی داشته باشند.

## ۳. پیشنهاد من: اول آزمایش، بعد انتخاب

من پیشنهاد می‌کنم فعلاً هیچ برنامه‌ای را نصب نکنیم. ابتدا یک آزمایش کوتاه با مدل‌های رایگان ابری انجام بدهیم و ببینیم کیفیت و تنوع پاسخ‌ها برایت کافی است یا نه. بعد اگر محدودیت سهمیه آزاردهنده بود یا خواستی مستقل از سرویس‌های آنلاین کار کنی، مدل محلی را راه می‌اندازیم.

برای شروع می‌توانی از [OpenRouter](https://openrouter.ai/models?max_price=0) مدل‌های رایگان را بررسی کنی؛ استفاده از API نیازمند ساخت حساب و کلید API است.

**نکته:** رایگان‌بودن به معنی نامحدودبودن نیست. اگر بخواهی چند عامل در چند دور به هم پاسخ دهند، مصرف درخواست‌ها سریع بالا می‌رود.

این مسیر به تو اجازه می‌دهد قبل از درگیرشدن با نصب و تنظیمات، خودِ کیفیت بحث چندعاملی را بسنجی.

| **بدنیست امتحان کردنش** |
| :--- |

عالی 😂 پس بیاییم یک آزمایش کوچک و واقعی انجام بدهیم؛ فعلاً بدون نصب چیزی روی کامپیوترت.

## قدم اول: دسترسی به مدل‌های رایگان

<box border radius="xl" padding={3} gap={3}>
  <row align="center" gap={3}>
    <AsyncImage query="OpenRouter AI models platform logo" aspectRatio="1:1" maxWidth="60px"/>
    <box flex="1" gap={1}>
      **<Entity category="software" value="OpenRouter" disambig="AI model API aggregator"/>**

      <text color="secondary" size="sm">دسترسی به چند مدل از یک سرویس</text>
      <text><Link url="https://openrouter.ai/models?max_price=0" title="دیدن مدل‌های رایگان"/></text>
    </box>
  </row>
  طبق صفحهٔ قیمت‌گذاری فعلی، پلن رایگان شامل مدل‌های رایگان و دسترسی به چت و API است؛ محدودیت عمومی آن برای مدل‌های رایگان ۵۰ درخواست در روز است، هرچند محدودیت ارائه‌دهندهٔ هر مدل هم ممکن است اعمال شود. <Cite refs={["turn182468search0","turn182468search5"]}/>
</box>

### کاری که فعلاً انجام بده

1. لینک بالا را باز کن و یک حساب بساز.
2. از میان مدل‌هایی که برچسب **Free** دارند، دو مدل متفاوت انتخاب کن.
3. هر دو را با یک سؤال یکسان آزمایش کن؛ هنوز لازم نیست API بسازی یا کلیدی را جایی وارد کنی.

برای آزمایش اول، این سؤال را به هر دو بده:

<box border radius="lg" padding={3} gap={2}>
  <text preserveWhitespace>یک شهر در برابر بحران کمبود منابع قرار گرفته است. سه راه وجود دارد:

۱. توزیع مساوی منابع بین همه
۲. تخصیص بیشتر به بخش‌هایی که بیشترین بازده را دارند
۳. حفظ ذخیرهٔ اضطراری و کاهش مصرف فعلی

کدام راه را انتخاب می‌کنی؟ فرضیاتت را مشخص کن، از انتخابت دفاع کن و قوی‌ترین ایراد به نظر خودت را هم بیان کن. اگر اطلاعات کافی نیست، بگو چه اطلاعاتی لازم داری.</text>
  <button block onClick={ => GenUI.copy("یک شهر در برابر بحران کمبود منابع قرار گرفته است. سه راه وجود دارد:\n\n۱. توزیع مساوی منابع بین همه\n۲. تخصیص بیشتر به بخش‌هایی که بیشترین بازده را دارند\n۳. حفظ ذخیرهٔ اضطراری و کاهش مصرف فعلی\n\nکدام راه را انتخاب می‌کنی؟ فرضیاتت را مشخص کن، از انتخابت دفاع کن و قوی‌ترین ایراد به نظر خودت را هم بیان کن. اگر اطلاعات کافی نیست، بگو چه اطلاعاتی لازم داری.")}>کپی سؤال آزمایشی</button>
</box>

بعد پاسخ‌های هر دو را همین‌جا بفرست. با هم بررسی می‌کنیم که آیا واقعاً تفاوت استدلال دارند یا فقط جواب‌های متفاوتی با ظاهر متفاوت تولید کرده‌اند.

**فعلاً سراغ نصب میزگرد نمی‌رویم.** اول کیفیت مدل‌ها را می‌سنجیم؛ بعد اتصالشان به یک اتاق بحث مشترک را انجام می‌دهیم.

| **باشه بزار ببینم چکار میکنن** |
| :--- |

باشه 😂 برو ببین این دوتا فیلسوف رایگان چه می‌کنن! 🏹⚖️

فقط وقتی جواب‌ها رو گرفتی، هر دو رو همین‌جا بفرست؛ حتی اگه یکی خیلی قانع‌کننده‌تر به نظر رسید.

من از سه جهت بررسی‌شون می‌کنم:

- **استقلال فکری:** واقعاً از دو زاویهٔ متفاوت به مسئله نگاه می‌کنن یا نه؟
- **کیفیت استدلال:** دلیل میارن یا فقط جواب خوش‌آب‌ورنگ تحویل می‌دن؟
- **نقد خود:** واقعاً ضعف نظر خودشون رو پیدا می‌کنن یا یه ایراد بی‌خطر و نمایشی می‌سازن؟

فعلاً دنبال این نیستیم که کدوم جواب درست‌تره؛ می‌خوایم بفهمیم آیا این مدل‌ها ظرفیت تبدیل‌شدن به اعضای یک میزگرد مفید رو دارن یا نه. 😁

| **Favicon for thinkingmachines**<br>**Thinking Machines: Inkling Small (free)**<br>**207B tokens**<br>**Inkling Small is an open-weight multimodal mixture-of-experts model from Thinking Machines Lab, with 12B active parameters out of 276B total. It is positioned as the smaller, more efficient member of the Inkling family and is suited for reasoning, coding, agentic workflows, retrieval-augmented generation, instruction following, and multilingual conversation.**<br>**by thinkingmachinesJul 30, 20261.05M context$0/M input tokens$0/M output tokens**<br>**Favicon for fish-audio**<br>**Fish Audio: S2.1 Pro Free (free)**<br>**18.8M tokens**<br>**S2.1 Pro Free is the no-cost variant of Fish Audio S2.1 Pro, intended for testing, prototyping, and low-volume applications. It provides the same synthesis capabilities without production latency or availability guarantees.**<br>**by fish-audioJul 29, 2026$0/M input tokens$0/M output tokens**<br>**Favicon for poolside**<br>**Poolside: Laguna S 2.1 (free)**<br>**Going away October 31, 2026**<br>**1T tokens**<br>**Laguna S 2.1 is the latest coding agent model from Poolside. Laguna S 2.1 is a 118B total parameter model with 8B active parameters, scoring 70.2% on Terminal-Bench 2.1 and 40.4% on DeepSWE, making it one of the strongest coding models in its category. Open-weight under the OpenMDW-1.1 license.  Laguna S 2.1 is designed for software engineering and agentic coding use cases, and you are responsible for confirming that it is appropriate for your intended application. Laguna S 2.1 is subject to the OpenMDW-1.1 License, and should be used consistently with Poolside's Acceptable Use Policy. We advise against circumventing Laguna S 2.1 safety guardrails without implementing substantially equivalent mitigations appropriate for your use case.  Please report security vulnerabilities or safety concerns to security@poolside.ai.  If you are using Laguna S 2.1 for free, we may use your inputs and outputs to train and improve our models.**<br>**by poolsideJul 21, 2026262K context$0/M input tokens$0/M output tokens**<br>**Favicon for thinkingmachines**<br>**Thinking Machines: Inkling (free)**<br>**381B tokens**<br>**Inkling is an open-weight multimodal mixture-of-experts model from Thinking Machines Lab, with 41B active parameters out of 975B total. It is designed for general-purpose reasoning, coding, agentic and tool-use systems, retrieval-augmented generation, instruction following, and multilingual conversational applications. Its native image and audio understanding supports multimodal analysis alongside text.**<br>**by thinkingmachinesJul 17, 20261.05M context$0/M input tokens$0/M output tokens**<br>**Favicon for nvidia**<br>**NVIDIA: Nemotron 3 Embed 1B (free)**<br>**931M tokens**<br>**NVIDIA Nemotron 3 Embed 1B is an open text embedding model from NVIDIA, optimized for high-throughput, low-latency retrieval. It is suited for enterprise search, RAG, code retrieval, and agentic retrieval workflows, retaining more than 95% of the 8B model’s accuracy in a smaller deployment footprint.**<br>**by nvidiaJul 16, 2026$0/M input tokens$0/M output tokens**<br>**Favicon for poolside**<br>**Poolside: Laguna XS 2.1 (free)**<br>**Going away October 31, 2026**<br>**94B tokens**<br>**Laguna XS 2.1 is the latest coding agent model in the 33B-A3B category from Poolside and a step forward from their Laguna XS.2 model (released in April 2026). It combines tool calling and reasoning capabilities with a compact footprint, offering a 256K context window and up to 32K output tokens. Quantized to FP8 for fast, cost-efficient agentic coding workflows.  Laguna XS 2.1 is designed for software engineering and agentic coding use cases, and you are responsible for confirming that it is appropriate for your intended application. Laguna XS 2.1 is subject to the OpenMDW-1.1 License, and should be used consistently with Poolside's Acceptable Use Policy. We advise against circumventing Laguna XS 2.1 safety guardrails without implementing substantially equivalent mitigations appropriate for your use case.  Please report security vulnerabilities or safety concerns to security@poolside.ai.  If you are using Laguna XS 2.1 for free, we may use your inputs and outputs to train and improve our models.**<br>**by poolsideJul 2, 2026262K context$0/M input tokens$0/M output tokens**<br>**Favicon for cohere**<br>**Cohere: North Mini Code (free)**<br>**171B tokens**<br>**North Mini Code is Cohere's first agentic coding model and the debut of its North family. A sparse mixture-of-experts model with 30B total parameters and 3B active, it is optimized for code generation, agentic software engineering, and terminal tasks, and is trained to generalize across agent harnesses such as OpenCode and SWE-Agent.  It offers a 256K-token context window with up to 64K tokens of output, supports interleaved reasoning and tool use via JSON schema, and is released open-weight under the Apache 2.0 license. Its small active-parameter footprint enables low-latency inference, including on local hardware.**<br>**by cohereJun 17, 2026256K context$0/M input tokens$0/M output tokens**<br>**Favicon for nvidia**<br>**NVIDIA: Llama Nemotron Rerank VL 1B V2 (free)**<br>**2.65B tokens**<br>**Llama Nemotron Rerank VL 1B V2 is a 1.7B multimodal reranking model from NVIDIA. It evaluates the relevance of document images and text against user queries, designed for vision RAG pipelines handling charts, tables, infographics, and mixed-media documents. Functions as a cross-encoder that accepts text queries paired with image, text, or combined document inputs, delivering approximately 6-7% recall improvements over embedding-only baselines on visual document retrieval benchmarks.**<br>**by nvidiaJun 9, 2026$0/M input tokens$0/M output tokens**<br>**Favicon for nvidia**<br>**NVIDIA: Nemotron 3.5 Content Safety (free)**<br>**2.24B tokens**<br>**NVIDIA Nemotron 3.5 Content Safety is a compact 4B-parameter multimodal guardrail model from NVIDIA, fine-tuned from Google Gemma-3-4B. It moderates both inputs to and responses from LLMs and VLMs, accepting text and image input and returning text output: a safe/unsafe classification for the user prompt and the response, safety category labels, and an optional reasoning trace. It covers 12 languages with a context window of up to 128K tokens.  It is suited for prompt and response moderation, content classification, safety pipelines, and enterprise AI guardrails with policy enforcement, and includes a togglable reasoning mode. It is part of the NVIDIA Nemotron family of open models for agentic AI.**<br>**by nvidiaJun 4, 2026128K context$0/M input tokens$0/M output tokens**<br>**Favicon for nvidia**<br>**NVIDIA: Nemotron 3 Ultra (free)**<br>**5.89T tokens**<br>**Health (#44)**<br>**NVIDIA Nemotron 3 Ultra is an open frontier-reasoning and orchestration model from NVIDIA, with 55B active parameters out of 550B total (MoE). Built on a hybrid Transformer-Mamba mixture-of-experts architecture, it supports text input and output with a context window of up to 1M tokens. It is suited for long-running agentic workflows, including agent orchestration, coding agents, deep research, and complex enterprise tasks.  It is particularly strong at multi-step reasoning and planning, with high-throughput inference designed for high-volume agent pipelines. It is part of the NVIDIA Nemotron family of open models for agentic AI.**<br>**by nvidiaJun 4, 20261M context$0/M input tokens$0/M output tokens**<br>**Favicon for nvidia**<br>**NVIDIA: Nemotron 3 Nano Omni (free)**<br>**43.1B tokens**<br>**NVIDIA Nemotron™ 3 Nano Omni is a 30B-A3B open multimodal model designed to function as a perception and context sub-agent in enterprise agent systems. It accepts text, image, video, and audio inputs and produces text output, enabling agents to perceive and reason across modalities in a single inference loop.  Built on a hybrid MoE Transformer-Mamba architecture with Conv3D video layers and Efficient Video Sampling (EVS), it delivers approximately 2× higher throughput and 2.5× lower compute for video reasoning versus separate vision + speech pipelines. It supports up to 300K context length and a 16,384 reasoning budget, with extended thinking enabled via reasoning.enabled on OpenRouter.**<br>**by nvidiaApr 28, 2026256K context$0/M input tokens$0/M output tokens**<br>**Favicon for google**<br>**Google: Gemma 4 26B A4B (free)**<br>**1.13B tokens**<br>**Gemma 4 26B A4B IT is an instruction-tuned Mixture-of-Experts (MoE) model from Google DeepMind. Despite 25.2B total parameters, only 3.8B activate per token during inference — delivering near-31B quality at a fraction of the compute cost. Supports multimodal input including text, images, and video (up to 60s at 1fps). Features a 256K token context window, native function calling, configurable thinking/reasoning mode, and structured output support. Released under Apache 2.0.**<br>**by googleApr 3, 2026262K context$0/M input tokens$0/M output tokens**<br>**Favicon for google**<br>**Google: Gemma 4 31B (free)**<br>**668M tokens**<br>**Gemma 4 31B Instruct is Google DeepMind's 30.7B dense multimodal model supporting text and image input with text output. Features a 256K token context window, configurable thinking/reasoning mode, native function calling, and multilingual support across 140+ languages. Strong on coding, reasoning, and document understanding tasks. Apache 2.0 license.**<br>**by googleApr 2, 2026262K context$0/M input tokens$0/M output tokens**<br>**Favicon for nvidia**<br>**NVIDIA: Llama Nemotron Embed VL 1B V2 (free)**<br>**489M tokens**<br>**The Llama Nemotron Embed VL 1B V2 embedding model is optimized for multimodal question-answering retrieval. The model can embed 'documents' in the form of image, text, or image and text combined. Documents can be retrieved given a user query in text form. The model supports images containing text, tables, charts, and infographics.**<br>**by nvidiaFeb 25, 2026$0/M input tokens$0/M output tokens** |
| :--- |

خوبه! 😂 این فهرست برای شروع خیلی به درد می‌خوره. از بین مدل‌هایی که فرستادی، برای آزمایش میزگرد من این دو را انتخاب می‌کنم:

<box gap={3}>
  <row align=start gap={3}>
    <AsyncImage query="Thinking Machines Lab Inkling Small AI model logo" aspectRatio="1:1" maxWidth="76px"/>
    <box flex="1" gap={1}>
      **۱. Inkling Small — عامل تحلیلگر**

      <text color="secondary" size="sm">۱۲ میلیارد پارامتر فعال · رایگان در OpenRouter</text>

      گزینهٔ اول برای آزمودن استدلال عمومی و تحلیل چندمرحله‌ای. اندازهٔ کل مدل بسیار بزرگ‌تر از تعداد پارامترهای فعال آن است، پس رایگان‌بودن API به معنی اجرای آسان آن روی کامپیوتر خودت نیست.
    </box>
  </row>
  <divider color="subtle"/>
  <row align=start gap={3}>
    <AsyncImage query="Google Gemma 4 26B A4B model logo" aspectRatio="1:1" maxWidth="76px"/>
    <box flex="1" gap={1}>
      **۲. Gemma 4 26B A4B — منتقد مستقل**

      <text color="secondary" size="sm">حدود ۳٫۸ میلیارد پارامتر فعال · رایگان در OpenRouter</text>

      انتخاب مناسبی برای مقایسهٔ اولیه است، چون خانواده و معماری آن با مدل اول متفاوت است. البته تفاوت معماری به‌تنهایی استقلال فکری یا کیفیت بالاتر را تضمین نمی‌کند.
    </box>
  </row>
</box>

## چطور آزمایش را انجام بدهیم؟

۱. در [OpenRouter](https://openrouter.ai/models?max_price=0) صفحهٔ هر دو مدل را باز کن و مطمئن شو هنوز رایگان و در دسترس‌اند.

۲. همان سؤال آزمایشی شهر و کمبود منابع را جداگانه برای هر دو بفرست. **پاسخ مدل اول را به مدل دوم نشان نده** تا ابتدا نظر مستقلشان را بسنجیم.

۳. هر دو پاسخ را اینجا بفرست. من اختلاف استدلال‌ها، فرضیات و کیفیت نقد خودشان را بررسی می‌کنم.

بعد از آن، دور دوم را اجرا می‌کنیم: هر مدل پاسخ مدل دیگر را می‌بیند و باید نقد کند. این مرحله به هدف اصلی تو نزدیک‌تر است.

**فعلاً سراغ Inkling اصلی، Nemotron 3 Ultra یا مدل‌های بسیار بزرگ نرویم.** برای اولین آزمایش نیازی به این پیچیدگی نداریم. و یک نکته: مدل Fish Audio که در فهرستت هست، مدل صوتی است و برای این آزمایش متنی انتخاب مناسبی نیست.

| **The free Inkling Small endpoint is only available for use with agentic harnesses. Do not upload any confidential information or personal data (e.g., voices and images of people's faces). Your usage of this free endpoint, including prompts and outputs, is logged and used to improve Thinking Machines Lab's models, products, and services. The logged session data will be disassociated from your account and other persistent identifiers before being used for these purposes.**<br>**By using this free endpoint, you agree to the TML Free Research API Terms of Service. For more information about Thinking Machines Lab's data processing practices, see this Privacy Notice.**<br>**Dismiss**<br>**Favicon for thinkingmachines**<br>**Thinking Machines: Inkling Small (free)**<br>**thinkingmachines/inkling-small:free**<br>**Model weights**<br>**Compare**<br>**API**<br>**Try this model**<br>**Inkling Small is an open-weight multimodal mixture-of-experts model from Thinking Machines Lab, with 12B active parameters out of 276B total. It is positioned as the smaller, more efficient member of the Inkling family and is suited for reasoning, coding, agentic workflows, retrieval-augmented generation, instruction following, and multilingual conversation.**<br>**Show less**<br>**Modalities**<br>**Price**<br>**Free**<br>**Context**<br>**1.0M**<br>**Released**<br>**Jul 30, 2026**<br>**Favicon for thinkingmachines**<br>**Thinking Machines: Inkling Small (free)**<br>**Compare**<br>**API**<br>**Try this model**<br>**Providers**<br>**Performance**<br>**Uptime**<br>**Benchmarks**<br>**Apps**<br>**Activity**<br>**FAQ**<br>**Explore**<br>**Providers**<br>**This model is hosted by one provider. OpenRouter forwards every request to it directly — no routing decisions to make.**<br>**Free**<br>**Reasoning effort**<br>**Latency / throughput**<br>**P50**<br>**P75**<br>**P90**<br>**P95**<br>**P99**<br>**Provider**<br>**Input /M**<br>**Output /M**<br>**Latency**<br>**Throughput**<br>**Uptime**<br>**Favicon for Thinking Machines**<br>**Thinking Machines**<br>**Free	Free	1.36s	98 tps**<br>**100.00%**<br>**Performance**<br>**Throughput is how fast the model writes (tokens per second — higher is better). Latency is total round-trip time (lower is better). TTFT is time-to-first-token — how long before you see anything appear (lower is better).**<br>**Throughput**<br>**98tok/s**<br>**P50, best across providers**<br>**Latency**<br>**1.36s**<br>**P50, best provider**<br>**All locations**<br>**Reasoning effort**<br>**All**<br>**1 week**<br>**Throughput**<br>**P50**<br>**Avg98 tok/s**<br>**P75**<br>**Avg61 tok/s**<br>**P90**<br>**Avg38 tok/s**<br>**P95**<br>**Avg28 tok/s**<br>**P99**<br>**Avg14 tok/s**<br>**Latency**<br>**P50**<br>**Avg1.38 s**<br>**P75**<br>**Avg2.09 s**<br>**P90**<br>**Avg3.21 s**<br>**P95**<br>**Avg4.45 s**<br>**P99**<br>**Avg10.26 s**<br>**E2E latency**<br>**P50**<br>**Avg3.68 s**<br>**P75**<br>**Avg5.61 s**<br>**P90**<br>**Avg8.85 s**<br>**P95**<br>**Avg12.22 s**<br>**P99**<br>**Avg26.17 s**<br>**AutoExacto benchmarks**<br>**GPQA DiamondTAU-Benchauto-routing86.7%62.0%DeepInfra86.9%58.5%**<br>**Tool call error rate**<br>**Thinking Machines**<br>**Avg5.94 %**<br>**Cache hit rate**<br>**Thinking Machines**<br>**Avg87.74 %**<br>**Uptime**<br>**Uptime is the percentage of the past 3 days that at least one provider was responding to requests. Availability is the percentage of time that inference was successfully served. OpenRouter continuously monitors and uses the next-best provider when one returns an error.**<br>**Uptime (3d)The model was reachable. Request routed to a provider.**<br>**100.00%**<br>**Availability (3d)The model returned inference from any provider. Errors and empty responses count against it.**<br>**99.35%**<br>**Availability over the last 3 days**<br>**Oct 25, 1 AM - Oct 28, 1 AM**<br>**Availability 99.35%**<br>**SunMonTueNow**<br>**Availability over the last 24 hours**<br>**Oct 27, 2:00 AM6:00 AM10:00 AM2:00 PM6:00 PM10:00 PM2:00 AM90%93%96%100%**<br>**OpenRouter Availability**<br>**99.40%**<br>**When an error occurs in an upstream provider, we can recover by routing to another healthy provider, if your request filters allow it. You can access per-provider uptime data programmatically through the Endpoints API. Learn more about our load balancing and provider routing options.**<br>**Benchmarks**<br>**Scores on standardized evaluations and this model’s own outputs on shared benchmark prompts. Higher percentages are better — and each rank shows where this model lands among the models evaluated on that source.**<br>**Benchmark score summary for Thinking Machines: Inkling Small (free) (Artificial Analysis and Vals AI)Source	Benchmark	Score**<br>**Artificial Analysis	Inkling Small Intelligence Index	25.7**<br>**Artificial Analysis	Inkling Small Coding Index	52.9**<br>**Artificial Analysis	Inkling Small Agentic Index	23.5**<br>**Artificial Analysis	Inkling Small GPQA Diamond	89.5%**<br>**Artificial Analysis	Inkling Small HLE	33.3%**<br>**Artificial Analysis	Inkling Small AA-LCR	75.7%**<br>**Artificial Analysis	Inkling Small τ-Bench Banking	18.8%**<br>**Artificial Analysis	Inkling Small GDPval-AA	31.6%**<br>**Artificial Analysis	Inkling Small CritPt	8.3%**<br>**Artificial Analysis	Inkling Small SciCode	49.7%**<br>**Artificial Analysis	Inkling Small Terminal-Bench 4.0	1.0%**<br>**Artificial Analysis	Inkling Small Terminal-Bench 2.1	55.1%**<br>**Artificial Analysis	Inkling Small AA-Omniscience Accuracy	33.2%**<br>**Artificial Analysis	Inkling Small AA-Omniscience Non-Hallucination Rate	37.0%**<br>**Vals AI	Inkling Small Code Migration v1.1	10.4%**<br>**Vals AI	Inkling Small CorpFin v2	69.6%**<br>**Vals AI	Inkling Small CyberBench v1.1	64.1%**<br>**Vals AI	Inkling Small EMB v1.1	40.8%**<br>**Vals AI	Inkling Small Finance Agent v2.1	44.8%**<br>**Vals AI	Inkling Small Vals Finance Index	36.3%**<br>**Vals AI	Inkling Small GPQA Diamond	83.6%**<br>**Vals AI	Inkling Small HLAB-Vals-1.1	2.9%**<br>**Vals AI	Inkling Small IOI	9.3%**<br>**Vals AI	Inkling Small LiveCodeBench	85.9%**<br>**Vals AI	Inkling Small LegalBench	83.0%**<br>**Vals AI	Inkling Small Vals Legal Index	57.8%**<br>**Vals AI	Inkling Small Legal Research Bench	25.5%**<br>**Vals AI	Inkling Small MedCode	37.9%**<br>**Vals AI	Inkling Small MedScribe	84.1%**<br>**Vals AI	Inkling Small MMLU Pro	85.6%**<br>**Vals AI	Inkling Small MortgageTax	62.3%**<br>**Vals AI	Inkling Small ProgramBench	0.5%**<br>**Vals AI	Inkling Small ProofBench v1.1	6.0%**<br>**Vals AI	Inkling Small SAGE	32.7%**<br>**Vals AI	Inkling Small SkillsBench	33.6%**<br>**Vals AI	Inkling Small SWE-bench	82.2%**<br>**Vals AI	Inkling Small Tax Agent Bench	15.4%**<br>**Vals AI	Inkling Small TaxEval v2	75.5%**<br>**Vals AI	Inkling Small Terminal-Bench 4.0	0.0%**<br>**Vals AI	Inkling Small Vals Index	27.6%**<br>**Vals AI	Inkling Small Vals Multimodal Index	50.1%**<br>**Vals AI	Inkling Small Vibe Code Bench v1.1	19.1%**<br>**Artificial Analysis**<br>**Vals AI**<br>**25.7**<br>**Artificial AnalysisIntelligence Index**<br>**Better than 79% of models compared**<br>**52.9**<br>**Artificial AnalysisCoding Index**<br>**Better than 64% of models compared**<br>**23.5**<br>**Artificial AnalysisAgentic Index**<br>**Better than 61% of models compared**<br>**Ranked #75 of 353**<br>**1. Claude Opus 5.5 57.6**<br>**Max 57.6**<br>**Xhigh 56.0**<br>**High 53.6**<br>**Medium 51.2**<br>**Low 42.3**<br>**2. Claude Sonnet 5.5 56.0**<br>**Max 56.0**<br>**Xhigh 51.9**<br>**High 46.8**<br>**Medium 40.8**<br>**Low 35.9**<br>**3. Kimi K3.1 Pro 55.1**<br>**4. Claude Fable 5.1 53.4**<br>**Max 53.4**<br>**Xhigh 53.2**<br>**High 51.2**<br>**Medium 48.9**<br>**Low 46.8**<br>**5. Qwen3.8 Max 53.4**<br>**6. GPT-6 Astra 52.7**<br>**Max 52.7**<br>**Xhigh 52.4**<br>**High 50.9**<br>**Medium 49.6**<br>**Low 45.8**<br>**7. Gemini 4 Argon (High) 52.6**<br>**8. GPT-6.1 Sol 51.8**<br>**Max 51.8**<br>**Xhigh 51.0**<br>**High 50.2**<br>**Medium 47.8**<br>**Low 42.1**<br>**74. Grok 4.20 0309 25.7**<br>**v2, Reasoning 25.7**<br>**Reasoning 25.2**<br>**Non-reasoning 14.6**<br>**v2, Non-reasoning 14.2**<br>**75. Inkling Small 25.7**<br>**76. Hy3 25.3**<br>**Hy3 25.3**<br>**preview, Reasoning 22.7**<br>**preview, Non-reasoning 17.0**<br>**Favicon for anthropic**<br>**#1Claude Opus 5.5**<br>**Favicon for anthropic**<br>**#2Claude Sonnet5.5**<br>**Favicon for moonshotai**<br>**#3Kimi K3.1 Pro**<br>**Favicon for anthropic**<br>**#4Claude Fable 5.1**<br>**Favicon for qwen**<br>**#5Qwen3.8 Max**<br>**Favicon for openai**<br>**#6GPT-6 Astra**<br>**Favicon for google**<br>**#7Gemini 4 Argon(High)**<br>**Favicon for openai**<br>**#8GPT-6.1 Sol**<br>**Favicon for x-ai**<br>**#74Grok 4.20 0309**<br>**Favicon for thinkingmachines**<br>**#75Inkling Small**<br>**Favicon for tencent**<br>**#76Hy30153045605856555353535352262625**<br>**See full rankings →**<br>**Reasoning**<br>**GPQA Diamond**<br>**Graduate-level scientific reasoning**<br>**#47 of 323 models**<br>**89.5%**<br>**HLE**<br>**Humanity's Last Exam**<br>**#72 of 339 models**<br>**33.3%**<br>**AA-LCR**<br>**Long context reasoning evaluation**<br>**#81 of 286 models**<br>**75.7%**<br>**τ-Bench Banking**<br>**Agentic tool use in a banking domain**<br>**#53 of 130 models**<br>**18.8%**<br>**GDPval-AA**<br>**Economically valuable tasks**<br>**#56 of 160 models**<br>**31.6%**<br>**CritPt**<br>**Research-level physics reasoning**<br>**#66 of 283 models**<br>**8.3%**<br>**Coding**<br>**SciCode**<br>**Python programming for scientific computing**<br>**#52 of 131 models**<br>**49.7%**<br>**Terminal-Bench 4.0**<br>**Agentic coding & terminal use**<br>**#55 of 126 models**<br>**1.0%**<br>**Terminal-Bench 2.1**<br>**Agentic coding & terminal use**<br>**#58 of 138 models**<br>**55.1%**<br>**Knowledge**<br>**AA-Omniscience Accuracy**<br>**Proportion of correctly answered questions**<br>**#69 of 281 models**<br>**33.2%**<br>**AA-Omniscience Non-Hallucination Rate**<br>**Rate of avoiding hallucination among non-correct responses**<br>**#100 of 281 models**<br>**37.0%** |
| :--- |

خب، این صفحه چند نکتهٔ مهم دارد که انتخاب ما را کمی تغییر می‌دهد. 😄

**اول از همه، Inkling Small رایگان است، اما رایگان بودنش به معنی استفادهٔ بدون محدودیت یا محرمانه نیست.** طبق هشدار خود OpenRouter، ورودی‌ها و خروجی‌های استفاده از این endpoint ثبت می‌شوند و برای بهبود مدل‌های Thinking Machines Lab استفاده خواهند شد. پس اطلاعات شخصی یا محرمانه واردش نکن.

## ارزیابی من از Inkling Small برای آزمایش ما

<box gap={3}>
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={3}>
      <icon name="brain" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **استدلال**

      امتیاز GPQA Diamond آن ۸۹٫۵٪ است؛ نشانه‌ای امیدوارکننده در یک آزمون دشوار علمی. اما این نتیجه به‌تنهایی نشان نمی‌دهد که مدل در بحث‌های چنددیدگاهی چقدر خوب عمل می‌کند.
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={3}>
      <icon name="messages-square" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **بحث و نقد متقابل**

      هنوز شواهد کافی نداریم که این مدل واقعاً دیدگاه مستقلی تولید می‌کند، ایرادهای اساسی دیگران را پیدا می‌کند یا فقط با لحنی متفاوت همان حرف‌ها را تکرار می‌کند. این دقیقاً همان چیزی است که باید آزمایش کنیم.
    </box>
  </row>
  <divider color="subtle" />
  <row align="start" gap={3}>
    <box background="surface-secondary" radius="lg" padding={3}>
      <icon name="gauge" size="xl" />
    </box>
    <box flex="1" gap={1}>
      **سرعت**

      سرعت گزارش‌شدهٔ ۹۸ توکن در ثانیه و تأخیر اولیهٔ حدود ۱٫۴ ثانیه مناسب به نظر می‌رسد؛ البته این اعداد تضمین نمی‌کنند که همهٔ درخواست‌ها با همین سرعت پاسخ بگیرند.
    </box>
  </row>
</box>

## اما یک مانع مهم وجود دارد

هشدار بالای صفحه می‌گوید:

> The free Inkling Small endpoint is only available for use with agentic harnesses.

یعنی این endpoint رایگان فقط برای استفاده از طریق یک **چارچوب اجرایی عامل‌محور (Agentic Harness)** در دسترس است. بنابراین ممکن است دکمهٔ **Try this model** برای گفت‌وگوی ساده کار نکند یا محدودیت داشته باشد. اگر چنین شد، لزوماً مشکل از تنظیمات تو نیست.

## قدم بعدی پیشنهادی من

فعلاً لازم نیست وارد ساخت سامانهٔ چندعاملی شویم. اول ببینیم این مدل واقعاً از چه راهی قابل استفاده است.

1. روی **Try this model** بزن.
2. اگر امکان ارسال پیام داد، همان مسئلهٔ شهر و کمبود منابع را که قبلاً تعیین کردیم، بدون تغییر برایش بفرست.
3. اگر خطا داد یا از تو خواست از یک harness استفاده کنی، متن خطا را بفرست تا مسیر مناسب را انتخاب کنیم.

یک نکتهٔ روش‌شناختی: حتی اگر Inkling Small پاسخ خوبی بدهد، برای هدف تو به یک مدل دوم با دیدگاه و ترجیحات متفاوت نیاز داریم. **دو مدل قوی الزاماً دو دیدگاه مستقل تولید نمی‌کنند.** معیار اصلی ما اختلاف واقعی در فرضیات، استدلال‌ها و تشخیص نقاط کور خواهد بود، نه صرفاً متفاوت بودن متن پاسخ‌ها.

| **Generation failed**<br>**thinkingmachines/inkling-small:free is only available on agentic harnesses. Try plugging it into a coding agent or productivity app listed on [https://openrouter.ai/apps](https://openrouter.ai/apps)** |
| :--- |

خب، پس مانع دقیقاً مشخص شد: **Inkling Small را نمی‌توان از چت سادهٔ OpenRouter آزمایش کرد؛ باید آن را به یک ابزار عامل‌محور وصل کنیم.** این خطا از پرامپت تو نیست.

دو مسیر داریم:

- **مسیر سریع‌تر:** فعلاً این مدل را کنار بگذاریم و مدل رایگان دیگری را که در چت مستقیم OpenRouter پاسخ می‌دهد انتخاب کنیم.
- **مسیر فنی‌تر:** یک harness راه‌اندازی کنیم تا چند مدل را در یک گفت‌وگوی مشترک قرار دهیم و پیام‌های یکدیگر را ببینند، نقد کنند و در صورت نیاز مخالفتشان را حفظ کنند.

با توجه به اینکه برای تو تفاوت واقعی دیدگاه‌ها مهم‌تر از صرفاً داشتن چند مدل است، مسیر دوم در نهایت مناسب‌تر است؛ چون می‌توانیم ترتیب بحث را هم طراحی کنیم: **تحلیل مستقل اولیه ← نقد متقابل ← پاسخ به نقدها ← گزارش اختلاف‌های حل‌نشده**.

## پیشنهاد عملی فعلی

به‌جای اینکه فعلاً وقت صرف اتصال Inkling Small کنیم، اول این مدل را امتحان کن:

<row align="start" gap={3}>
  <AsyncImage query="Google Gemma AI model logo" aspectRatio="1:1" maxWidth="76px" />
  <box flex="1" gap={1}>
    **<Entity value="Google Gemma 4 26B A4B" category="software" disambig="Google DeepMind open-weight language model" />**

    <badge color="success">رایگان در فهرست فعلی</badge>

    طبق صفحهٔ OpenRouter، این مدل از طریق رابط مستقیم API قابل استفاده است و ابزار فراخوانی هم پشتیبانی می‌کند؛ محدودیت سهمیهٔ رایگان همچنان وجود دارد. <Cite refs={["turn784822search2"]}/>

    [باز کردن Gemma 4 در OpenRouter](https://openrouter.ai/google/gemma-4-26b-a4b-it:free)
  </box>
</row>

اگر از چت مستقیم پاسخ گرفتیم، آزمایش اول را انجام می‌دهیم. بعد یک مدل دوم انتخاب می‌کنیم و پاسخ‌های اولیه را مستقل می‌گیریم.

اما اگر هدف نهایی‌ات همان میزگرد چندعاملی واقعی است، پیشنهاد من این است که پس از این تست کوچک، یک چارچوب متن‌باز روی کامپیوترت بسازیم یا راه‌اندازی کنیم که از APIهای رایگان استفاده کند. این‌طوری به‌جای وابستگی به یک رابط چت، کنترل می‌کنیم کدام عامل چه زمانی پاسخ دیگران را ببیند و چطور آن‌ها را نقد کند.

| **Generation failed**<br>**(Google AI Studio) Rate limit exceeded. Please try again shortly. Consider adding your own API key to accumulate your own rate limits.** |
| :--- |

😂 خب، دومین مانع هم روشن شد: این بار مدل قابل استفاده است، اما سهمیهٔ رایگان Google AI Studio پر شده. این لزوماً به معنی تمام شدن سهمیهٔ شخصی تو نیست؛ ممکن است محدودیت سراسری یا محدودیت همان مدل باشد.

به نظرم بهتر است فعلاً مدل‌به‌مدل بین صفحات چت جابه‌جا نشویم. این دقیقاً همان جایی است که یک میزگرد چندعاملی با APIهای قابل‌تعویض ارزش پیدا می‌کند.

**دو مسیر عملی داریم:**

1. **بدون برنامه‌نویسی:** مدل رایگان دیگری در OpenRouter امتحان کنیم؛ ممکن است باز هم به محدودیت سهمیه یا دسترسی برخورد کنیم.
2. **راه‌حل پایدارتر:** یک میزگرد کوچک روی ویندوزت بسازیم که از چند مدل رایگان پشتیبانی کند، پاسخ‌های اولیه را مستقل بگیرد و سپس پاسخ‌ها را برای نقد متقابل به عوامل بدهد. اگر یک مدل محدود شد، بتوانیم آن را عوض کنیم.

با توجه به اینکه با Python و PowerShell کار کرده‌ای، مسیر دوم برایت شدنی است؛ ولی باید صادق باشم: **رایگان بودن APIها تضمین نمی‌کند که همیشه در دسترس باشند یا سهمیهٔ کافی داشته باشند.**

من مسیر دوم را ترجیح می‌دهم. اول یک نسخهٔ ساده با دو عامل و سه مرحلهٔ بحث می‌سازیم، بدون اجبار به توافق نهایی. بعد کیفیت اختلاف دیدگاه‌ها را آزمایش می‌کنیم.

| **# Selected text:**<br>**## Selection 1**<br>**من مسیر دوم را ترجیح می‌دهم. اول یک نسخهٔ ساده با دو عامل و سه مرحلهٔ بحث می‌سازیم، بدون اجبار به توافق نهایی. بعد کیفیت اختلاف دیدگاه‌ها را آزمایش می‌کنیم.**<br>**## My request:**<br>**خب چاره ای نیست ببینیم چی میشه** |
| :--- |

پس شروع کنیم. نسخهٔ اولیه را ساختم؛ فعلاً بدون رابط گرافیکی و بدون نصب کتابخانه‌های اضافی، تا اگر خطایی پیش آمد راحت‌تر بفهمیم از کجاست.

<box border radius="xl" padding={4} gap={3}>
  <row align="center" gap={3}>
    <box background="surface-secondary" radius="lg" size="48px" align="center" justify="center">
      <icon name="code-2" size="2xl" />
    </box>
    <box flex="1" gap={1}>
      <title size="lg">Two-Agent Debate</title>
      <text color="secondary" size="sm">نسخهٔ آزمایشی اول · Python · ویندوز</text>
    </box>
  </row>
  <text>این برنامه دو مدل را در سه مرحله وارد بحث می‌کند:</text>
  <list marker="number" gap={2}>
    <list-item>**تحلیل مستقل:** هر مدل مسئله را جداگانه بررسی می‌کند و پاسخ دیگری را نمی‌بیند.</list-item>
    <list-item>**نقد متقابل:** هر مدل پاسخ اولیهٔ دیگری را می‌خواند و نقد می‌کند.</list-item>
    <list-item>**پاسخ نهایی:** هر مدل به نقدها جواب می‌دهد و اختلاف‌های حل‌نشده را مشخص می‌کند.</list-item>
  </list>
  [دریافت فایل Python](files/001-دریافت فایل Python.bin)
</box>

## قدم اول: اتصال به OpenRouter

۱. وارد [OpenRouter](https://openrouter.ai/) شو و در صورت نیاز حساب بساز.

۲. از بخش [API Keys](https://openrouter.ai/settings/keys) یک کلید API بساز. **کلید را برای من نفرست و در فایل برنامه هم قرار نده.** برنامه هنگام اجرا می‌تواند آن را به‌صورت مخفی از تو بگیرد.

۳. فایل بالا را در یک پوشه، مثلاً `C:\Users\Zardakh\two-agent-debate` قرار بده.

۴. PowerShell را در همان پوشه باز کن و اجرا کن:

```powershell
python .\two_agent_debate.py
```

اگر فرمان `python` کار نکرد، این را امتحان کن:

```powershell
py .\two_agent_debate.py
```

برنامه دو شناسهٔ مدل پیشنهادی دارد؛ می‌توانی با زدن Enter همان‌ها را بپذیری یا شناسه‌های دیگری وارد کنی. فهرست مدل‌های رایگان مرتب تغییر می‌کند و محدودیت سهمیه هم وجود دارد؛ بنابراین هنوز تضمینی نیست هر دو مدل در اولین اجرا پاسخ بدهند. <Cite refs={["turn471519search0","turn471519search2"]}/>

وقتی برنامه موضوع بحث را خواست، می‌توانی پرامپت آزمایشی شهر و کمبود منابع را وارد کنی و در خطی جداگانه بنویسی `END`.

**نکته:** خروجی‌ها در پوشهٔ `debate_results` ذخیره می‌شوند. چون سیاست ثبت و استفاده از داده‌ها بین ارائه‌دهندگان متفاوت است، فعلاً موضوعات آزمایشی و غیرمحرمانه وارد کن.

فعلاً همین مرحله را انجام بده. اگر برنامه خطا داد، متن کامل خطا را بفرست؛ اگر اجرا شد، پاسخ‌های دو عامل را بررسی می‌کنیم و می‌بینیم آیا واقعاً اختلاف دیدگاه دارند یا فقط دو پاسخ شبیه به هم تولید می‌کنند.

| **TWO-AGENT DEBATE — prototype**<br>**==================================================================**<br>**Uses OpenRouter API. Free endpoints can be rate-limited or unavailable.**<br>**Do not enter confidential or personal information in the topic.**<br>**OpenRouter API key (input hidden):** |
| :--- |

عالی، برنامه درست اجرا شده و الان منتظر کلید API است. 👍

در این مرحله:

1. کلیدی را که از [OpenRouter API Keys](https://openrouter.ai/settings/keys) ساخته‌ای، در PowerShell وارد کن و Enter بزن. هنگام تایپ، نمایش داده نمی‌شود؛ این طبیعی است.
2. بعد برنامه نام دو مدل را می‌پرسد. فعلاً می‌توانی با زدن Enter، مدل‌های پیش‌فرض را امتحان کنی.
3. اگر خطای مدل ناموجود یا محدودیت سهمیه دیدی، متن خطا را بفرست تا اصلاحش کنیم.

**دو نکته:**
- کلید API را اینجا در چت نفرست.
- فعلاً به حساب اعتبار پولی اضافه نکن؛ هدف ما آزمایش مسیر رایگان است.

وقتی به مرحلهٔ انتخاب مدل رسیدی، اگر خواستی قبل از ادامه خروجی همان بخش را بفرست تا با هم بررسی کنیم.

| **چرا هیچی تایپ نمیکنه؟** |
| :--- |

طبیعیه 😂 رمزت رو مخفی کرده، نه اینکه برنامه هنگ کرده باشه!

در PowerShell وقتی برنامه از `getpass` استفاده می‌کنه، **هنگام تایپ کلید API هیچ چیزی نمایش داده نمی‌شه؛ نه حروف، نه ستاره و نه نقطه.**

الان این کار رو انجام بده:

1. کلید API رو تایپ یا Paste کن؛ حتی اگر صفحه کاملاً خالیه.
2. کلید رو اینجا نفرست.
3. کلید رو که وارد کردی، `Enter` بزن.

اگر درست پیش بره، به مرحلهٔ انتخاب مدل می‌رسی.

اگر Paste هم کار نکرد، بهم بگو؛ یک راه جایگزین داریم.

| **==================================================================**<br>**TWO-AGENT DEBATE — prototype**<br>**==================================================================**<br>**Uses OpenRouter API. Free endpoints can be rate-limited or unavailable.**<br>**Do not enter confidential or personal information in the topic.**<br>**OpenRouter API key (input hidden):**<br>**Model A [google/gemma-4-31b-it:free]:** |
| :--- |

عالی 😂 کلید رو پذیرفته و از مرحلهٔ اول رد شدیم؛ حالا برنامه منتظر انتخاب مدل A است.

فعلاً **Enter بزن** تا مدل پیش‌فرض را امتحان کنیم:

`google/gemma-4-31b-it:free`

بعد از آن، برنامه شناسهٔ مدل B را می‌پرسد. آنجا هم فعلاً Enter بزن تا مدل دوم پیش‌فرض انتخاب شود.

اگر یکی از مدل‌ها خطای سهمیه یا شناسهٔ نامعتبر داد، متن کامل خطا را بفرست. هنوز لازم نیست چیزی را تغییر بدهیم.
