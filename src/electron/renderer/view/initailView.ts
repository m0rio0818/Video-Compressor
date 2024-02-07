export class InitialView {
    static create() {
        let root = document.getElementById("app");
        root!.innerHTML = `
        <div class="pt-20">
            <div class="max-w-2xl w-full mx-auto">
                <div class="relative py-2">
                    <label for="video_select" class="cursor-pointer text-center">Select MP4: </label>
                    <div id="selected_video"></div>
                    <input id="video_select" accept="mp4" type="file" class="absolute inset-0 w-full h-full opacity-0 cursor-pointer">
                    <div class="mx-auto w-10/12 sm:w-1/3  bg-blue-500 hover:bg-blue-600 active:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-300 text-white p-2 rounded-full text-center ">Choose Video</div>
                </div>
                <div class="bg-gray-300">
                    <label for="conversion" class="cursor-pointer text-center">変換方法: </label>
                    <div class="relative inline-block mx-auto text-left">
                        <select id="conversion" class="px-4 py-2 focus:outline-none">
                            <option disabled selected>選択してください</option>
                            <option value="compression">圧縮</option>
                            <option value="resolution">解像度変更</option>
                            <option value="aspect">アスペクト変更</option>
                            <option value="mp3">音声に変換</option>
                            <option value="gif">GIF作成</option>
                            <option value="webm">WEBEM作成</option>
                        </select>
                    </div>
                </div>
                <div id="optionArea">
                </div>
                <div class="flex justify-center pt-10"> 
                    <button id="convert" class="w-10/12 sm:w-1/3 text-center bg-blue-500  hover:bg-blue-600 active:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-300 p-2 rounded-full text-white">変換</button>
                </div>
            </div>
        </div>
            `;
    }
}