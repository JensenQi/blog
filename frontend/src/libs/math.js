import Quill from 'quill';

const KaTeX = Quill.import('formats/formula');

class LaTex extends KaTeX {
    static create(value) {
        let node = document.createElement("span");
        if (typeof value === 'string') {
            this.tex2img(value, function (output) {
                node.innerHTML = output
            })
        }
        return node;
    }

    static value(domNode) {
        return domNode.getAttribute('data-value');
    }

    static tex2img(formula, callback) {
        MathJax.Hub.Queue(function () {
            let wrapper = MathJax.HTML.Element("span", {}, `$$${formula}$$`);
            MathJax.Hub.Typeset(wrapper, function () {
                let svg = wrapper.getElementsByTagName("svg")[0];
                svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
                let image = new Image();
                image.src = 'data:image/svg+xml;base64,' + window.btoa(unescape(encodeURIComponent(svg.outerHTML)));
                image.onload = function () {
                    let canvas = document.createElement('canvas');
                    canvas.width = image.width;
                    canvas.height = image.height;
                    let context = canvas.getContext('2d');
                    context.drawImage(image, 0, 0);
                    let img = `<img src="${canvas.toDataURL('image/png')}" alt="${formula}"/>`;
                    callback(img);
                };
            });
        })
    }


}

export default LaTex
