const initialState = {
    currentTable: [],
    totalCostInDollars: 0,
    totalCostInRubles: 0
};

const reducer = (state = initialState, action) => {
    switch (action.type) {
        case 'SETTABLE':
            return {
                ...state,
                currentTable: action.payload
            }
        case 'TOTALCOSTINDOLLARS':
            return {
                ...state,
                totalCostInDollars: action.payload
            }
        case 'TOTALCOSTINRUBLES':
            return {
                ...state,
                totalCostInRubles: action.payload
            }
        default:
            return state
    }
}

export default reducer;