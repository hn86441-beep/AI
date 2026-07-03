import asyncio
from flask import Flask, render_template_string, request, jsonify
import g4f
import nest_asyncio

# حل مشكلة تداخل الـ Asyncio مع بيئة تشغيل Flask
nest_asyncio.apply()

app = Flask(__name__)

# واجهة المستخدم (HTML + CSS + JS) مصممة بالكامل وتدعم العربية ومتجاوبة مع الهواتف
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مساعد الذكاء الاصطناعي المجاني</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            width: 100%;
            max-width: 600px;
        }
        h1 {
            color: #1a73e8;
            text-align: center;
            margin-bottom: 5px;
        }
        p.subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 25px;
            font-size: 14px;
        }
        textarea {
            width: 100%;
            height: 120px;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 8px;
            box-sizing: border-box;
            resize: vertical;
            font-size: 16px;
        }
        button {
            width: 100%;
            background-color: #1a73e8;
            color: white;
            padding: 14px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
            font-weight: bold;
            transition: background 0.3s;
        }
        button:hover {
            background-color: #1557b0;
        }
        .result-box {
            margin-top: 20px;
            padding: 15px;
            background-color: #f8f9fa;
            border-right: 5px solid #1a73e8;
            border-radius: 6px;
            display: none;
            white-space: pre-wrap;
            line-height: 1.6;
            color: #333;
        }
        .loading {
            text-align: center;
            color: #666;
            display: none;
            margin-top: 15px;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>مساعد الذكاء الاصطناعي المجاني 🤖</h1>
    <p class="subtitle">يعمل تلقائياً وبدون أي مفاتيح تشغيل (No API Key)</p>
    
    <textarea id="question" placeholder="اكتب سؤالك هنا بوضوح..."></textarea>
    <button onclick="sendQuestion()">إرسال السؤال للذكاء الاصطناعي</button>
    
    <div id="loading" class="loading">⏳ جاري الاتصال بالذكاء الاصطناعي وتوليد الإجابة...</div>
    <div id="result" class="result-box"></div>
</div>

<script>
    async function sendQuestion() {
        const question = document.getElementById('question').value;
        const resultBox = document.getElementById('result');
        const loadingDiv = document.getElementById('loading');
        
        if (!question.trim()) {
            alert('من فضلك اكتب سؤالاً أولاً!');
            return;
        }

        loadingDiv.style.display = 'block';
        resultBox.style.display = 'none';

        try {
            const response = await fetch('/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ question: question })
            });

            const data = await response.json();
            
            loadingDiv.style.display = 'none';
            resultBox.style.display = 'block';

            if (data.answer) {
                resultBox.innerText = data.answer;
                resultBox.style.borderRightColor = '#1a73e8';
                resultBox.style.backgroundColor = '#f8f9fa';
            } else {
                resultBox.innerText = 'عذراً، حدث خطأ: ' + (data.error || 'خطأ غير معروف');
                resultBox.style.borderRightColor = '#f44336';
                resultBox.style.backgroundColor = '#ffebee';
            }
        } catch (error) {
            loadingDiv.style.display = 'none';
            resultBox.style.display = 'block';
            resultBox.innerText = 'فشل الاتصال بالخادم الداخلي.';
            resultBox.style.borderRightColor = '#f44336';
            resultBox.style.backgroundColor = '#ffebee';
        }
    }
</script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_question = data.get('question', '')

    if not user_question:
        return jsonify({'error': 'الرجاء كتابة سؤال'}), 400

    try:
        # استخدام g4f للبحث تلقائياً عن مزود مجاني شغال بدون API Key لنموذج افتراضي ممتاز
        response = g4f.ChatCompletion.create(
            model=g4f.models.default, # يختار تلقائياً أفضل نموذج متاح ومستقر (مثل GPT-4o أو Claude المتاح مجاناً)
            messages=[
                {"role": "system", "content": "أنت مساعد ذكي ومفيد تجيب على الأسئلة باللغة العربية بدقة وبشكل مفصل وبدون كتابة مقدمات طويلة."},
                {"role": "user", "content": user_question}
            ]
        )
        
        answer = str(response)
        
        # حماية في حال فشل المزود المجاني مؤقتاً
        if not answer or answer == "None" or len(answer.strip()) == 0:
            return jsonify({'error': 'المزود المجاني مشغول حالياً، يرجى إعادة محاولة إرسال السؤال مجدداً.'}), 500
            
        return jsonify({'answer': answer})
    
    except Exception as e:
        return jsonify({'error': f"خطأ أثناء جلب الإجابة: {str(e)}"}), 500

if __name__ == '__main__':
    print("*" * 50)
    print("جاري تشغيل الموقع بنجاح!")
    print("افتح متصفحك واذهب إلى: http://127.0.0.1:5000")
    print("*" * 50)
    app.run(debug=True)

