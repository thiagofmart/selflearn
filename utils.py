import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
import streamlit.components.v1 as components
import os

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)


def load(path_file):
    with open(path_file, "r") as file:
        string = file.read()
        return string

def get_sin_df(frequency=1, amplitude=1, period=2*np.pi, hshift=0, vshift=0):
    f = lambda x: np.sin(x)
    x_arr = np.arange(0, period, 0.1) + hshift
    y_arr = amplitude * f(frequency * (x_arr)) + vshift
    df = pd.DataFrame(
        data=y_arr,
        index=x_arr,
        columns=["f(x) = sin(x)", ],
    )
    return df

def generate_motion_df(size_of_entities, plane_dim, max_velocity):
    velocity_vectors = np.random.uniform(0, max_velocity, size_of_entities*2) # generate x and y velocitys vector based on max_velocity
    df_entities = pd.DataFrame({
    "x":np.ceil(np.random.rand(size_of_entities)*plane_dim[0]*0.8+20.0), #x coordinate between [0-plane_dim[0]]
    "y":np.ceil(np.random.rand(size_of_entities)*plane_dim[1]*0.8+20.0), #y coordinate between [0-plane_dim[1]]
    "r":np.concatenate(([20], np.random.rand(size_of_entities-1)*25+2), ), #radius between [0-1]
    'vi':velocity_vectors[0:size_of_entities], # divide the vector into two and gets the first part
    "vj":velocity_vectors[size_of_entities:], # divide the vector into two and gets the second part
    })
    colisions = df_entities.apply(
        lambda row: _getEntitiesColisionsTotalVectorialSum(row, df_entities), 
        axis=1
        ).tolist()
    df_entities = df_entities if len(np.unique(colisions))==1 else generate_motion_df(size_of_entities, plane_dim, max_velocity)
    return df_entities

def _identifyBorderColision(row, plane_dim):
        """
        -1 for border colision and 1 for no border colision
        -1 because we can revert the module of the vector when colisions happens
        1 to still the same vector direction when no colision happens
        """
        left_b = -1 if (row['x']-row['r'] <= 0) else 1
        right_b = -1 if (row['x']+row['r'] >= plane_dim[0]) else 1
        top_b = -1 if (row['y']-row['r'] <= 0) else 1
        bottom_b = -1 if (row['y']+row['r'] >= plane_dim[1]) else 1
        return np.array([left_b, right_b, top_b, bottom_b])

def _getEntitiesColisionsTotalVectorialSum(row, df_entities):
        """
        The strategy that I will adopt to infer that a colision occurs between two entities,

        I will validate if the distance between the central point of a entity is <= sum of the 
        radius of entity one and entity two
        
        """
        x0, y0, r0, vi0, vj0 = row['x'], row['y'], row['r'], row['vi'], row['vj']
        df = df_entities.drop(row.name) #df without the entity that is being validated
        #selecting all the entities that the central point distance are <= sum of radius
        selection = df.loc[df.apply(
            lambda _row: True if np.sqrt((x0-_row['x'])**2+(y0-_row['y'])**2) <= r0+_row['r'] else False,
            axis=1), ["vi", "vj"]
        ]
        if not selection.empty:
            selection[['vi', 'vj']] = selection.apply(lambda _row: [_row['vi']-vi0, _row['vj']-vj0], axis=1).tolist()
            vectorial_sum = selection.sum().tolist()
        else:
            vectorial_sum = [0, 0]
        return vectorial_sum

async def update_motion_df(df_entities, plane_dim):
    """
    1 - Verify Colision with border -> reverse the velocity vector direction
    2 - Verify Colision with another entity -> sum up the vectors of the entities
    """
    #Identifying border colision
    df_entities[[
        "colision_lb", "colision_rb", "colision_tb", "colision_bb", 
        ]
    ] = df_entities.apply(lambda row: _identifyBorderColision(row, plane_dim), axis=1).tolist() # explanation of why use tolist() https://stackoverflow.com/questions/64280284/how-to-use-apply-in-a-pandas-dataframe-slice-to-set-values-of-multiple-columns
    #Reverting the vectors direction where border colision happens
    df_entities[[
        "vi", "vj",
    ]] = df_entities.apply(
        lambda row: [
            row["vi"]*row['colision_lb']*row['colision_rb'], 
            row["vj"]*row['colision_tb']*row['colision_bb'],
            ], 
        axis=1,
    ).tolist()
    # get the total sum of vectors that must be applied for each entity that has colision
    df_entities[[
        "vi_tosumup", "vj_tosumup"
    ]] = df_entities.apply(
        lambda row: _getEntitiesColisionsTotalVectorialSum(row, df_entities), 
        axis=1
        ).tolist()
    # applies the sum of the vectors
    df_entities["vj"] += df_entities['vj_tosumup']
    df_entities["vi"] += df_entities['vi_tosumup']
    # changing the entities coordinates
    df_entities["x"] += df_entities["vi"]
    df_entities["y"] += df_entities["vj"]
    return df_entities[['x', 'y', 'r', 'vi', 'vj']]

async def create_image(plane_dim, df_entities):
    image = Image.new('RGBA', (plane_dim[0]+1, plane_dim[1]+1))
    draw = ImageDraw.Draw(image)
    #board
    draw.rectangle([(0,0), (plane_dim[0],plane_dim[1])], fill="white", outline="red", width=1)
    for row in df_entities.iterrows():
        x, y, r = row[1]["x"], row[1]["y"], row[1]["r"]
        draw.ellipse(
            [ #defining coordinates of
                (x-r, y-r), # x0, y0
                (x+r, y+r) # x1, y1
            ], # where x0 <= x1 and y0 <= y1
            fill = 'blue', 
            outline ='blue'
        )
    return image


def render_footer():
    variables = {
    "github": "https://github.com/thiagofmart",
    "linkedin": "https://www.linkedin.com/in/thiago-ferreira-martins-45004b191/",
    "instagram": "https://www.instagram.com/thiago_fmart/",
    "email": "thiago.fmartins@outlook.com",
    "link_style":'color:white; text-decoration: none; margin-left:20px; margin-right:20px;',
    }
    javascript = f'<script language="javascript">{load("javascript/index.js")}</script>'
    components.html(javascript+load("html/myFooter.html").format(
    github=variables["github"],
    linkedin=variables["linkedin"],
    instagram=variables["instagram"],
    email=variables["email"],
    link_style=variables["link_style"],
    ),
    height=35
)
