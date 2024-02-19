import * as net from "net";

class Client {
    public HEADER_BYTES_SIZE: number = 64;
    public buffer: number = 4096;
    public dPath: string = "./video";
    private address: string;
    private server_address: string;
    private port: number;
    private server_port: number;
    private socket: net.Socket | null;

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

    connect(): void {
        this.socket = net.createConnection({
            host: this.address,
            port: this.port,
        });

        this.socket.on("data", (data) => {
            console.log(`Recoved data from  server ${data}`)
        })

        this.socket.on("end", ()=>{
            console.log("Disconnected from server")
        })
    }

    send(data : string) : void {
        if (!this.socket){
            console.error("SOcket is not connected");
            return;
        }
        this.socket.write(data);
    }

    disconnect(): void {
        if (!this.socket){
            console.error("Socket is not connected!");
            return;
        }
        this.socket.end();
        this.socket = null;
    }
}

const client = new Client("0.0.0.0", "0.0.0.0", 9050, 9001);
