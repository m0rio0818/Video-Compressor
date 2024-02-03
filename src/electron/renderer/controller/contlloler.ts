// import { InitialView } from "../view/initailView";

export class Controller {
    static renderInitialPage() {
        const root = document.getElementById("app");
        root!.innerHTML = `
            <div class="pt-14 ">
                <div class="max-w-2xl w-full mx-auto bg-sky-950">
                    <div class="bg-red-200">
                        <p class="text-2xl text-center tracking-widest">MP4 Videoを選択してください。</p>
                        <div class="mt-10 flex flex-col lg:flex-row justify-center gap-y-4 lg:gap-x-6">
                            <input id="name-input" name="email" value="" type="email" required placeholder="名前を入力してください" class="text-md sm:flex items-center w-full lg:w-72 text-left space-x-3 px-4 h-12 bg-white ring-1 ring-slate-900/10 hover:ring-slate-300 focus:outline-none focus:ring-2 focus:ring-sky-500 shadow-sm rounded-lg text-slate-400 dark:bg-slate-800 dark:ring-0 dark:text-slate-300 dark:highlight-white/5 dark:hover:bg-slate-700" autocomplete="off" id="nuid-0">
                            <button id="start-button" class="text-sm bg-slate-900 hover:bg-slate-700 focus:outline-none focus:ring-2 focus:ring-slate-400 focus:ring-offset-2 focus:ring-offset-slate-50 text-white font-semibold h-12 px-6 rounded-lg w-full flex items-center justify-center sm:w-auto dark:bg-sky-500 dark:highlight-white/20 dark:hover:bg-sky-400">はじめる</button>
                        </div>
                    </div>
                    <div class="bg-red-500">
                        <p>a</p>
                    </div>
                </div>
            </div>
            `;
    }

    static animation() {
        document.getElementById("card-1")!.classList.add("card1-animation");
        document.getElementById("card-2")!.classList.add("card2-animation");
        document.getElementById("card-3")!.classList.add("card3-animation");
        document.getElementById("card-4")!.classList.add("card4-animation");
        document.getElementById("card-5")!.classList.add("card5-animation");
    }
}
