import _, {
    get as _get,
    reduce as _reduce,
    setWith as _setWith,
    isEqual as _isEqual,
} from "lodash";
import { acquireAccessToken } from '../../lib/AuthUtils';
import { env } from '../../config/env'

// stop page refresh by default on clicks
export const stopURLPropagation = (e) => {
    e.preventDefault();
}

/* manage json response from endpoints */
export const handleJsonResponse = (response) => {
    if(response.ok) {
        switch(response.status) {
            case 226:
            case 208:
            case 204:
                return response.status;
            default:
                return response.json().then(res => {
                    return res;
                });
        }
    } else {
        if(_isEqual(getAbsURL('dwb/saved-queries/'), _get(response, 'url', ''))) {
            return response.json().then(res => {
                return res;
            });
        }
        return [];
    }
}

export const handleRequestHeaders = async (method='GET') => {
    const apiBearerToken = await acquireAccessToken();
    return {
        method: method,
        headers: {
            Authorization: `Bearer ${apiBearerToken}`,
            'Strict-Transport-Security': 'max-age=63072000; includeSubDomains; preload',
        },
    };
}

export const getAbsURL = (path) => _.get(env, "API_URL") + path

/* convert array of object into map of object grouped by keyss */
export const arrayToMapByKeys = (array, key, ikey, value) => {
    return array.reduce((map, val) => {
        (map[val[key]] = map[val[key]] || {})[val[ikey]] = val[value];
        return map;
    }, {});
};

/* convert array of object into map of key values pairs */
export const arrayToMap = (array, key, value) => {
    return array.reduce((map, val) => {
        map[val[key]] = val[value];
        return map;
    }, {});
};

/* convert array of objects into map of objects */
export const arrayToMapOfObjects = (array, key, initialState={}) => {
    return array.reduce((map, val) => {
        map[val[key]] = val;
        return map;
    }, initialState);
};

export const arrayWithIdAsKey = (array, key) => {
    return array.map((value) => {
        return { [value[key]]: value };
    });
}

export const arrayToMapWithVals = (array) => {
    return array.reduce((map, val) => {
        map[val] = val;
        return map;
    }, {});
}

/** Format number */
export const formatNumber = (number) => {
    return Math.round((number + Number.EPSILON) * 100) / 100
}

export const isOnlyNumber = (value, numberOnlyFilter = false) => {
    return numberOnlyFilter ? 
        /^-?[0-9,.]*$/.test(value)
    : 
        /^[0-9,.]*$/.test(value)
}

export const isOnlyFloatNumber = (value) => {
    return /^[0-9]*[.]?[0-9]*$/.test(value);
}

export const getEventValue = (event, convertEmptyToZero=false) => {
    if(_.get(event, ['target', 'value']) === '') {
        return convertEmptyToZero ? 0 : '';
    }

    const newValue = _.get(event, ['target', 'value']);
    if (
        newValue &&
        isOnlyFloatNumber(newValue)
    ) {
        return limitStringNumberDecimalPoints(newValue, convertEmptyToZero);
    }

    return null;
};

export const  limitStringNumberDecimalPoints = (numValue) => {
    if (numValue) {
        return (_.endsWith(_.trimEnd(numValue, 0), '.') && !_.endsWith(numValue, '.0')) ?
            (_.isEqual(numValue, '.') ? '0' + numValue : numValue) :
             _.floor(numValue, 1);
    }
    return null;
}

export const formatInputNumber = (number) => {
    return (_.endsWith(_.trimEnd(number, 0), '.') && !_.endsWith(number, '.00')) ? number :_.floor(number, 2);
}

export const formatOneDecimal = (number) => {
    return (_.endsWith(_.trimEnd(number, 0), '.') && !_.endsWith(number, '.0')) ? number :_.floor(number, 1);
}

export const formatNoDecimal = (number) => _.floor(number, 0);

export const formatNoDecimalRound = (number) => _.round(number, 0);

export const downloadCsv = (csv, filename) => {
	// CSV FILE
	const csvFile = new Blob([csv], { type: "text/csv" });
	// Download link
	const downloadLink = document.createElement("a");
	// File name
	downloadLink.download = filename;
	// We have to create a link to the file
	downloadLink.href = window.URL.createObjectURL(csvFile);
	// Make sure that the link is not displayed
	downloadLink.style.display = "none";
	// Add the link to your DOM
	document.body.appendChild(downloadLink);
	// Lanzamos
	downloadLink.click();
};

export const checkUserPermissions = (permissionGroup, userRoles) => {
    return !_.isEmpty(_.intersection(permissionGroup, userRoles));
}

 export const formatToDecimalPoint = (numberToFormat, decimalPoint=1) => numberToFormat ? +parseFloat(numberToFormat).toFixed(decimalPoint) : 0;

 export const arrayToMapWithKeys = (data, itemkey) => _reduce(data, (reportData, reportItem) => {
    _setWith(
        reportData,
        _get(reportItem, itemkey, 0),
        reportItem,
        Object
    )
    return reportData;
}, {});

export const getValueFromEvent = (event, decimalPoint=2) => {
    let returnValue = null;
    if (
        _.get(event, ['target', 'value']) &&
        isOnlyNumber(_.get(event, ['target', 'value']))
    ) {
        const eventValues = _.get(event, ['target', 'value']).split('.');
        if (eventValues.length > 1) {
            returnValue = _.get(eventValues, 0) + '.';
            if(_.get(eventValues, 1) !=='' ) {
                returnValue += _.get(eventValues, 1).slice(0, decimalPoint);
            }
        } else {
            returnValue = parseInt(_.get(event, ['target', 'value']))
        }
    } else if(_.get(event, ['target', 'value']).trim() === '') {
        returnValue = 0;
    }

    return returnValue;
}

export const buildURIQuery = (params={}) => {
    return '?' + _.join(_.reduce(_.keys(params), (queryParams, paramName) => {
        const paramValue = _.get(params, paramName, null);
        if(!_.isNull(paramValue)) {
            queryParams.push(
                paramName + '=' + encodeURIComponent(paramValue)
            )
        }
        return queryParams
    }, []), '&')
}

export const numberOnlyFilter = (eventValue, currValue=0, numberOnlyFilter = false) => {
    let newValue = currValue;
    if (eventValue && isOnlyNumber(eventValue, numberOnlyFilter)) {
        const eventValues = eventValue.split('.');
        if (eventValues.length > 1) {
            newValue = _.get(eventValues, 0) + '.';
            if(_.get(eventValues, 1) !=='' ) {
                newValue += _.get(eventValues, 1).slice(0, 2);
            }
        } else {
            if(numberOnlyFilter && eventValue === "-"){
                newValue = 0;
            }
            else{
                newValue = parseInt(eventValue)
            }
        }
    } else if(eventValue.trim() === '') {
        newValue = 0;
    }
    return newValue;
}

export const alphaNumericFilter = (eventValue) => {
    const newValue = _.replace(eventValue, /[^0-9a-zA-Z .-]/gi, '');
    return newValue;
}

export const alphaNumericWithSpecialFilter = (eventValue) => {
    const newValue = _.replace(eventValue, /[^0-9a-zA-Z .,()%;:"'-]/gi, '');
    return newValue;
}