// import * as net from "net";
// const net = require("net");
// import fs from "fs";

class Client {
    public HEADER_BYTES_SIZE: number = 64;
    public buffer: number = 4096;
    public dPath: string = "./video";
    private address: string;
    private server_address: string;
    private port: number;
    private server_port: number;
    private socket: any;

    constructor(
        address: string,
        server_address: string,
        port: number,
        server_port: number
    ) {
        this.address = address;
        this.server_address = server_address;
        this.port = port;
        this.server_port = server_port;
        this.socket = null;
    }

    findData(path: string): void {
        const fs = require("fs");
        fs.readFile("./../video/sample.mp4", (err :any, data : string) => {
            if (err) {
                console.error("Error reading file:", err);
                return;
            }
            // const bytes = Array.from(data);
            // バイト単位で処理
            this.send(data);
            console.log(data);
        });
    }

    makeHeader() : string {
        
    }

    connect(): void {
        this.socket = net.createConnection({
            host: this.server_address,
            port: this.server_port,
        });

        this.socket.on("data", (data) => {
            console.log(`Recoved data from  server ${data}`);
            this.socket.end();
        });

        this.socket.on("end", () => {
            console.log("Disconnected from server");
        });
    }

    send(data: string): void {
        if (!this.socket) {
            console.error("SOcket is not connected");
            return;
        }
        this.socket.write(data);
    }

    disconnect(): void {
        if (!this.socket) {
            console.error("Socket is not connected!");
            return;
        }
        this.socket.end();
        this.socket = null;
    }
}

const client = new Client("0.0.0.0", "0.0.0.0", 9050, 9001);
client.connect();
client.findData("a");

// client.send("HELLO WORLD");
