import time

# --- CareBridge: AI Senior Care Health Agent ---

print("=" * 50)
print("     WELCOME TO CAREBRIDGE AI HEALTH AGENT      ")
print("=" * 50)

# 1. बुजुर्ग माता-पिता (Senior Citizen) का डेटा सेट करना
parent_name = "Anwar Hussain"
print(f"\n[AI Status] Monitoring health data for: {parent_name}")
time.sleep(1)

# 2. यूज़र (या मशीन) से हेल्थ वाइटल्स इनपुट लेना
# यहाँ हम मान लेते हैं कि बैकग्राउंड एजेंट ने ये रीडिंग ली हैं:
sys_bp = 145       # सिस्टोलिक ब्लड प्रेशर (ऊपर का बीपी)
sugar_level = 190  # ब्लड शुगर लेवल (रैंडम)

print("\n--- Current Health Vitals Reading ---")
print(f"Blood Pressure : {sys_bp} mmHg")
print(f"Blood Sugar    : {sugar_level} mg/dL")
print("-" * 38)
time.sleep(1)

# 3. AI Agent Decision Logic (बैकग्राउंड में स्वायत्त रूप से निर्णय लेना)
print("\n[AI Agent] Analyzing readings in the background...")
time.sleep(1.5)

is_emergency = False
alert_message = ""

# बीपी और शुगर की जांच करने का नियम
if sys_bp >= 140 or sugar_level >= 180:
    is_emergency = True
    alert_message = f"🚨 ALERT: Critical vitals detected for {parent_name}!"
    if sys_bp >= 140:
        alert_message += f"\n   - High BP: {sys_bp} mmHg (Normal is < 120)"
    if sugar_level >= 180:
        alert_message += f"\n   - High Sugar: {sugar_level} mg/dL (Normal is < 140)"
else:
    alert_message = f"✅ Status Normal: {parent_name}'s health is stable."

# 4. आउटपुट और स्मार्ट नोटिफिकेशन (Autonomous Trigger)
if is_emergency:
    print("\n" + "!" * 50)
    print("⚠️  CRITICAL HEALTH EMERGENCY DETECTED ⚠️")
    print("!" * 50)
    print(alert_message)
    print("\n[AI Action] Sending urgent SMS & Email to Ilma Bano...")
    print("[AI Action] Preparing automatic doctor appointment request...")
    print("!" * 50)
else:
    print("\n" + "=" * 50)
    print(alert_message)
    print("[AI Action] Everything looks good. Keeping background sync active.")
    print("=" * 50)

print("\n" + "=" * 50)
print("  CareBridge SDK Agent Run Completed Successfully ")
print("=" * 50)
