# SmartGuide AI 2.0

Arabic-language camera object-detection **student research prototype**, responsive on mobile and laptop. Uses TensorFlow.js and the pretrained COCO-SSD Lite MobileNet model. The app displays boxes, labels, position **within the image** (left/center/right), confidence, and Arabic browser speech synthesis; it can optionally vibrate on mobile. Video is processed locally in the browser after loading the model and is not uploaded by this app.

## Safety

**Not an assistive navigation or collision-avoidance device.** This model cannot reliably identify walls, stairs, drop-offs, holes, or clear walking routes, and does **not** estimate real-world object distances or provide safe turn-by-turn directions. Never rely on it while walking alone. Test stationary with a sighted supervisor; continue using established mobility aids.

## Deployment

Publish the repository using **Settings → Pages → Build and deployment → Deploy from a branch → main / (root)**. The site will be at `https://zidiz08-dot.github.io/smartguide-ai-2/` after Pages publishes successfully. HTTPS is required for camera permission. Internet access is needed to load the TensorFlow.js libraries and the object detection model.

## Supported detection

Pretrained [COCO-SSD](https://github.com/tensorflow/tfjs-models/tree/master/coco-ssd) recognizes up to 80 COCO object categories, such as chairs, dining tables, people, bottles, and bags. It is **not trained** to recognize stairs or walls. A model label describes the detected object only. Screen-left/screen-right descriptions must **never** be interpreted as safe navigation instructions. Confidence is the model's score, not a calibrated safety probability.

## Test

Use Chrome or Edge on HTTPS. Grant camera permission, allow model download, aim at a chair/table in a safe stationary setting. Try voice and camera switching. Browser Arabic speech depends on operating-system voices.