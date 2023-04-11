// Created by Parker Jackim
// Custom JavaScript for Lichess desktop integration using nativefier


function remove(selector) {
    var element = document.querySelector(selector);
    if (element) {
        element.parentNode.removeChild(element);
    }
}


// Remove top navbar
// remove("#top");

// Remove these classes after the page has loaded.
// Sole purpose is to make it look pretty for a small window
// window.addEventListener('onload', function() {

// });

// Get the body element
const body = document.body;


const board = document.querySelector('body.board-layout');
board.setAttribute('style', 'padding-top: 8.5rem!important;');

const graph = document.querySelector('rated-sidebar-mobile-order-3');
graph.setAttribute('style', 'padding-top: 0!important;');

// body.style.paddingTop = "8.5rem!important";

// body.addEventListener('onmouseover', function() {
//     console.log("Body hover");
//     body.style.paddingTop = "8.5rem";
// })



// Create a new div element with the class "custom-scrollbar"
const wrapper = document.createElement('div');
wrapper.classList.add('custom-scroll');

// Move all the child elements of the body to the new div
while (body.firstChild) {
    wrapper.appendChild(body.firstChild);
}

// Add the new div to the body
body.appendChild(wrapper);


// const svgElement = document.querySelector("cg-board");
// const pathElements = svgElement.querySelectorAll("rect");

// pathElements.forEach(rect => {
//     if (rect.getAttribute("fill") === "#dee3e6") {
//         rect.style.fill = "#424650";
//     } else {
//         rect.style.fill = "#2D313D";
//     }

// });