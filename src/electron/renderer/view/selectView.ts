export class selectView {
    static clearArea() {
        let option = document.getElementById("optionArea")!;
        console.log(option);
        if (option) {
            option.innerHTML = ``;
        }
    }

    static clearCustomArea() {
        let custom_area = document.getElementById("custom_input_area");
        custom_area!.innerHTML = "";
    }

    static compressoinView() {
        let option = document.getElementById("optionArea")!;
        option.innerHTML = `
        <div class="max-w-md mx-auto p-8">
            <h2 class="text-2xl  mb-4 text-center">Quality</h2>
            <label class="flex items-center space-x-2">
                <input type="radio" value="high" name="radioOption" class="text-sky-500 form-radio focus:ring-sky-500 h-4 w-4">
                <span class="text-gray-800">High</span>
            </label>
        
            <label class="flex items-center space-x-2">
                <input type="radio" value="normal" name="radioOption" class="text-sky-500 form-radio focus:ring-sky-500 h-4 w-4">
                <span class="text-gray-800">Normal</span>
            </label>
        
            <label class="flex items-center space-x-2">
                <input type="radio" value="low" name="radioOption" class="text-sky-500 form-radio focus:ring-sky-500 h-4 w-4">
                <span class="text-gray-800">Low</span>
            </label>
        </div>
        `;
    }

    static resolutionView() {
        let option = document.getElementById("optionArea")!;
        option.innerHTML = `
        <div class="max-w-md mx-auto p-8">
            <label for="resolution" class="cursor-pointer text-center">解像度選択: </label>
            <div class="relative inline-block mx-auto text-center">
                <select id="resolution" class="px-4 py-2 focus:outline-none">
                    <option disabled selected>選択してください</option>
                    <option value="720p">720p</option>
                    <option value="1080p">1080p</option>
                    <option value="wqhd">WQHD</option>
                    <option value="4k">4K</option>
                    <option value="8k">8K</option>
                    <option value="custom">カスタム</option>
                </select>
            </div>
        </div>
        <div id="custom_input_area"  class="bg-blue-400"></div>

        `;
    }

    static customInput() {
        let custom_area = document.getElementById("custom_input_area");
        let customInput = `
        <div class="flex flex-col sm:flex-row w-full p-3">
            <div class="w-full sm:w-1/2 bg-pink-300 py-1 px-2 sm:pr-2">
                <input type="text" id="width" class="w-full bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="W" required>
            </div>
            <div class="flex items-center  justify-center h-full py-1 ">
                <p class="text-2xl text-center"> × </p>
            </div>
            <div class="w-full sm:w-1/2 bg-orange-400 py-1 px-2  sm:pl-2">
                <input type="number" id="height" class="w-full bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="H">
            </div>
        </div>
        `;
        custom_area!.innerHTML = customInput;
    }

    static aspectView() {
        let option = document.getElementById("optionArea")!;
        option.innerHTML = `
        <div class="flex flex-col sm:flex-row w-full p-3">
            <div class="w-full sm:w-1/2 bg-pink-300 py-1 px-2 sm:pr-2">
                <input type="text" id="width" class="w-full bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="W" required>
            </div>
            <div class="flex items-center  justify-center h-full py-1 ">
                <p class="text-2xl text-center"> : </p>
            </div>
            <div class="w-full sm:w-1/2 bg-orange-400 py-1 px-2  sm:pl-2">
                <input type="number" id="height" class="w-full bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="H">
            </div>
        </div>
    `;
    }

    static mp3View() {
        let option = document.getElementById("optionArea")!;
        option.innerHTML = `

    `;
    }

    static gifView() {
        let option = document.getElementById("optionArea")!;
        option.innerHTML = `

    `;
    }
    static webmView() {
        let option = document.getElementById("optionArea")!;
        option.innerHTML = `

    `;
    }
}
