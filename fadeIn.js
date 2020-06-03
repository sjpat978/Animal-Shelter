    const faders = document.querySelectorAll('.fade-in');
    const sliders = document.querySelectorAll('.left-selector');
    const appearOps = {
        threshold: 0,
        // makes sure there is a delay based on our location in the document
        rootMargin: "0px 0px -200px 0px"
    };
    //monitors changes in intersection of target element with other elements
    const appearOnScroll = new IntersectionObserver(function(entries, appearOnScroll) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            }
            else {
                entry.target.classList.add('appear');
                // stop looking at something once you've done your job.
                appearOnScroll.unobserve(entry.target);
            }
        });
    }, appearOps);
    faders.forEach(fader => {
        appearOnScroll.observe(fader);
    });
    sliders.forEach(slider => {
        appearOnScroll.observe(slider);
    })


    
