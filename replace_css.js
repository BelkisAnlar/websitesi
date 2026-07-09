const fs = require('fs');

const cssContent = fs.readFileSync('style.css', 'utf8');

const newSliderCss = `/* Slider CSS Wrapper */
.services-slider-wrapper {
  margin-bottom: 8rem;
}

.slider-container {
  position: relative;
  width: 100%;
  max-width: 1000px;
  height: 400px;
  margin: 0 auto;
  perspective: 1000px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.slider-track {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  display: flex;
  justify-content: center;
  align-items: center;
}

.slider-card {
  position: absolute;
  width: 280px;
  height: 350px;
  background-color: #ffffff;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(29, 93, 155, 0.08);
  transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.6s ease, z-index 0.6s ease;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  user-select: none;
}

.slider-card img {
  width: 100%;
  height: 220px;
  object-fit: cover;
  border-bottom: 3px solid var(--accent);
}

.slider-card h3 {
  padding: 1rem;
  text-align: center;
  font-size: 1.2rem;
  color: var(--secondary);
  margin: 0;
}

.slider-card .hidden-desc {
  display: none;
}

/* Coverflow positioning */
.slider-card.active {
  transform: translateX(0) scale(1.1) translateZ(0);
  z-index: 5;
  opacity: 1;
}

.slider-card.next-1 {
  transform: translateX(25%) translateZ(-100px) rotateY(-20deg);
  z-index: 4;
  opacity: 0.8;
}

.slider-card.next-2 {
  transform: translateX(50%) translateZ(-200px) rotateY(-30deg);
  z-index: 3;
  opacity: 0.5;
}

.slider-card.prev-1 {
  transform: translateX(-25%) translateZ(-100px) rotateY(20deg);
  z-index: 4;
  opacity: 0.8;
}

.slider-card.prev-2 {
  transform: translateX(-50%) translateZ(-200px) rotateY(30deg);
  z-index: 3;
  opacity: 0.5;
}

.slider-card.hidden {
  transform: translateZ(-300px);
  z-index: 1;
  opacity: 0;
  pointer-events: none;
}

/* Buttons */
.slider-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: var(--secondary);
  color: #fff;
  border: none;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  font-size: 1.2rem;
  cursor: pointer;
  z-index: 10;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
  transition: background 0.3s ease, transform 0.2s ease;
}

.slider-btn:hover {
  background: var(--accent);
  transform: translateY(-50%) scale(1.1);
}

.slider-btn.prev-btn {
  left: 0;
}

.slider-btn.next-btn {
  right: 0;
}

/* Dynamic Description Box */
.slider-description-box {
  max-width: 800px;
  margin: 2rem auto 0;
  background: #ffffff;
  padding: 2rem;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(29, 93, 155, 0.08);
  border-top: 4px solid var(--accent);
  text-align: center;
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.4s ease, transform 0.4s ease;
}

.slider-description-box.fade-in {
  opacity: 1;
  transform: translateY(0);
}

.slider-description-box h3 {
  font-size: 1.8rem;
  color: var(--secondary);
  margin-bottom: 1rem;
}

.slider-description-box .short-desc {
  font-size: 1.1rem;
  color: var(--text-dark);
  font-weight: 600;
  margin-bottom: 1.5rem;
}

.slider-description-box .long-desc {
  color: var(--text-muted-dark);
  font-size: 1rem;
  line-height: 1.6;
  text-align: left;
}

.slider-description-box .long-desc p {
  margin-bottom: 0.8rem;
}

.slider-description-box .long-desc strong {
  color: var(--secondary);
}

/* Mobile Adjustments */
@media (max-width: 768px) {
  .slider-card.next-2, .slider-card.prev-2 {
    opacity: 0;
    pointer-events: none;
    transform: translateZ(-300px);
  }
  .slider-card.next-1 {
    transform: translateX(40%) translateZ(-100px) rotateY(-15deg);
  }
  .slider-card.prev-1 {
    transform: translateX(-40%) translateZ(-100px) rotateY(15deg);
  }
  .slider-btn.prev-btn { left: -10px; }
  .slider-btn.next-btn { right: -10px; }
}`;

// Use regex to replace .services-grid ... up to .hotel-banner-glass
// We need to match from .services-grid { down to but not including /* Hotel Section Glassmorphism */
const pattern = /\.services-grid\s*{[\s\S]*?(?=\/\*\s*Hotel Section Glassmorphism\s*\*\/)/;
const newCss = cssContent.replace(pattern, newSliderCss + '\n\n');

fs.writeFileSync('style.css', newCss, 'utf8');
console.log('Successfully replaced CSS content');
