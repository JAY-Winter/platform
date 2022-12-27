import React, {useState} from "react";
import styled from "styled-components";
import GlobalStyle from "../modules/GlobalStyle/GlobalStyle";

const Select = () => {
    const [active, setActive] = useState(false);

    const dropDownHandler = () => {
        setActive(!active);
    }

    return <Box>
        <GlobalStyle/>
        <DropDown onClick={dropDownHandler}>
            HELP ME
            <LeftIcon className="arrow" isActive={active}/>
            <RightIcon className="arrow" isActive={active}/>

            <Items isActive={active}>
                <Elem isActive={active}>
                    <SubElem></SubElem>HEL_...</Elem>
                <Elem isActive={active}>
                    <SubElem></SubElem>HEL_...</Elem>
                <Elem isActive={active}>
                    <SubElem></SubElem>HEL_...</Elem>
                <Elem isActive={active}>
                    <SubElem></SubElem>HEL_...</Elem>
            </Items>
        </DropDown>
    </Box>
}

export default Select;

const SubElem = styled.span `
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: var(--primary-color-light);
    z-index: -1;
    transform: rotate(160deg);
    transform-origin: right;
    transition: var(--trans-03);
`

const Elem = styled.span < {
    isActive: boolean
} > `
    position: relative;
    left: ${props => props.isActive
    ? '0'
    : '100%'};
    display: flex;
    font-size: 16px;
    padding: 8px 15px;
    color: var(--text-color);
    border-radius: 6px;
    z-index: 1;
    background: var(--body-color);
    overflow: hidden;
    transition: var(--trans-03);

    &:hover {}

    &:hover span {
        transform: rotate(0deg);
    }
`

const Items = styled.div < {
    isActive: boolean
} > `
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: fit-content;
    margin-top: 43px;
    overflow: hidden;
    visibility: ${props=> props.isActive? "visible":"hidden"};
    transition: var(--trans-03);
`

const RightIcon = styled.span < {
    isActive: boolean
} > `
transform: ${props => props.isActive
    ? "rotate(-135deg)"
    : "rotate(-45deg)"};
`

const LeftIcon = styled.span < {
    isActive: boolean
} > `
    left: 4px;
    transform: ${props => props.isActive
    ? "rotate(135deg)"
    : "rotate(45deg)"};
`

const DropDown = styled.div `
    position: relative;
    width: 100%;
    height: 40px;
    background: var(--body-color);
    border: solid 2px var(--primary-color-light);
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 6px;
    cursor: pointer;

    & .arrow {
        top: 2px;
        position: relative;
        display: inline-block;
        width: 10px;
        height: 3.5px;
        background: var(--primary-color-light);
        border-radius: 40px;
        transition: var(--trans-05);
    }    
`

const Box = styled.div `
    position: relative;
    width: 150px;
    height: fit-content;
`