#!/usr/bin/env python
# coding: utf-8

# In[73]:


from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("diagram-explore", show=False):
    ELB("lb") >> EC2("web") >> RDS("userdb")
# %%
