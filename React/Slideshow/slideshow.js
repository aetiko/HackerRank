import React, { useState } from "react";

function Slides({ slides }) {
  const [currentSlide, setCurrentSlide] = useState(0);
  const nextSlide = () => {
    if(currentSlide < slides.length -1){
      setCurrentSlide(currentSlide+1);
    }
  }
  const prevSlide = () => {
    if(currentSlide > 0){
      setCurrentSlide(currentSlide-1);
    }
  }
  const restart = () => {
    setCurrentSlide(0);
  }
  return (
    <div>
      <div id="navigation" className="text-center">
        <button data-testid="button-restart" onClick={restart} disabled = {currentSlide === 0} className="small outlined">
          Restart
        </button>
        <button data-testid="button-prev" disabled = {currentSlide === 0} onClick= {prevSlide} className="small">
          Prev
        </button>
        <button data-testid="button-next" disabled = {currentSlide === slides.length -1 } onClick={nextSlide} className="small">
          Next
        </button>
      </div>
      <div id="slide" className="card text-center">
        <h1 data-testid="title">{slides[currentSlide].title}</h1>
        <p data-testid="text">{slides[currentSlide].text}</p>
      </div>
    </div>
  );
}

export default Slides;
