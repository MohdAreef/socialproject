function scrollToSection(sectionId) {
    var section = document.querySelector(sectionId);
    section.scrollIntoView({ behavior: 'smooth' });
}