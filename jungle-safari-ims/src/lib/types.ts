export interface User {
    id: number;
    username: string;
    full_name: string;
    contac_no: string;
    email: string;
    store: Store | undefined;
    role: 'owner' | 'manager' | 'cashier' | undefined;
}

export interface Store {
    id: number;
    name: string;
    address: string;
}