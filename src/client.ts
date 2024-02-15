import { Socket } from "net";

class Client {
    public HEADER_BYTES_SIZE: number = 64;
    public buffer: number = 4096;
    public dPath: string = "./video";
    public address: string;
    public server_address: string;
    public port: number;
    public server_port: number;
    public socket : Socket;

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
    }

    connect(): void {}
}

const client = new Client("0.0.0.0", "0.0.0.0", 9050, 9001);
