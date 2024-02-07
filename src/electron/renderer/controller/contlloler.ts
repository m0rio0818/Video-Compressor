import { InitialView } from "../view/initailView.js";
import { selectView } from "../view/selectView.js";

export class Controller {
    static renderInitialPage() {
        InitialView.create();
        Controller.selectMode();
    }

    static selectMode() {
        let filepath: string = "";
        let videoSelect = document.getElementById(
            "video_select"
        ) as HTMLInputElement;
        videoSelect?.addEventListener("change", () => {
            let files = videoSelect?.files ?? [];
            if (files) {
                filepath = files[0].path;
                let textArea = document.getElementById("selected_video");
                textArea!.innerHTML = files[0].name;
                console.log("File path:", filepath); // ここでファイルのパスを取得
            } else {
                console.log("No file selected.");
            }
        });

        let conversionSelect = document.getElementById(
            "conversion"
        ) as HTMLInputElement;

        conversionSelect.addEventListener("change", () => {
            let typeOfConvresion = conversionSelect.value;
            console.log(typeOfConvresion);

            if (typeOfConvresion == "compression") {
                selectView.clearArea();
                selectView.compressoinView();
                Controller.changeQuality();
            } else if (typeOfConvresion == "resolution") {
                selectView.clearArea();
                selectView.resolutionView();
                Controller.changeResolution();
            } else if (typeOfConvresion == "aspect") {
                selectView.clearArea();
                selectView.aspectView();
            } else if (typeOfConvresion == "mp3") {
                selectView.clearArea();
                // selectView.mp3View();
            } else if (typeOfConvresion == "gif") {
                selectView.clearArea();
                selectView.gifView();
            } else if (typeOfConvresion == "webm") {
                selectView.clearArea();
                selectView.webmView();
            } else {
                selectView.clearArea();
            }
        });

        let convertButton = document.getElementById(
            "conversion"
        ) as HTMLInputElement;

        convertButton.addEventListener("click", () => {});
    }

    static changeQuality() {
        const radioButtons = document.querySelectorAll('input[type="radio"]');
        radioButtons.forEach(button => {
            console.log(button);
            button.addEventListener("change", () => {
                const selectedValue = document.querySelector('input[name="radioOption"]:checked')
                console.log(selectedValue.value);
            })
        })
    }

    static changeResolution() {
        const resolutionLevel = document.getElementById("resolution");
        resolutionLevel!.addEventListener("change", () => {
            selectView.clearCustomArea();
            if (resolutionLevel!.value == "custom") {
                selectView.customInput();
            }
        });
    }
}
