/** @jsxRuntime classic */
/** @jsx jsx */
import { jsx, css } from '@emotion/react';
import CircularProgress from '@mui/material/CircularProgress';

const LoadingIcon = () => {
    return (
        <div css={circular_progress_css}>
            <CircularProgress />
        </div>
    )
}

export default LoadingIcon

const circular_progress_css = css({
	position: 'flex',
    marginLeft: "48%",
    marginTop: "15%",
})
