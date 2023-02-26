export interface GoodsSchema {
    name: string,
    price: number,
    purchases: number,
    amount: string,
    category: {
        name: string
    },
}